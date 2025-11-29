import logging
from pathlib import Path

from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    MetricsCollectedEvent,
    RoomInputOptions,
    WorkerOptions,
    cli,
    metrics,
    tokenize,
)
from livekit.plugins import murf, silero, google, deepgram, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel

logger = logging.getLogger("agent")

env_path = Path(__file__).parent.parent / ".env.local"
load_dotenv(env_path)

GAME_MASTER_PROMPT = """You are a legendary Game Master running an epic fantasy D&D-style adventure. The player is interacting with you via voice.

UNIVERSE: A mystical realm called Eldoria, filled with ancient magic, fearsome dragons, mysterious dungeons, and legendary treasures. The world is at a crossroads - an ancient evil stirs in the Shadowlands, and heroes are needed.

YOUR ROLE AS GAME MASTER:
- You describe vivid, immersive scenes with rich sensory details
- You voice NPCs with distinct personalities and speaking styles
- You present challenges, puzzles, and combat encounters
- You react dynamically to the player's choices and improvise accordingly
- You maintain tension, mystery, and excitement throughout the adventure

STORY RULES:
- Always describe the current scene before asking what the player does
- End every response with a clear prompt for the player's next action, like "What do you do?" or "How do you respond?"
- Remember the player's past decisions and reference them when relevant
- Introduce interesting NPCs, items, and locations as the story progresses
- Create meaningful consequences for the player's choices
- Build toward mini-arcs: discovering secrets, escaping danger, defeating enemies, finding treasures

TONE: Dramatic and immersive, but with occasional moments of humor. Make the player feel like the hero of their own epic tale.

FORMATTING: Speak naturally without special formatting, emojis, or asterisks. Your speech should flow like a skilled storyteller narrating an adventure.

BEGIN THE ADVENTURE: When the player first speaks, welcome them as an adventurer arriving at the Crossroads Inn in the village of Millbrook. A mysterious hooded figure has been asking about brave souls willing to investigate strange occurrences in the nearby Whispering Woods. Set the scene and ask if they wish to learn more."""


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=GAME_MASTER_PROMPT)


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    ctx.log_context_fields = {"room": ctx.room.name}

    session = AgentSession(
        stt=deepgram.STT(model="nova-3"),
        llm=google.LLM(model="gemini-2.5-flash"),
        tts=murf.TTS(
            voice="en-US-matthew",
            style="Conversation",
            tokenizer=tokenize.basic.SentenceTokenizer(min_sentence_len=2),
            text_pacing=True,
        ),
        turn_detection=MultilingualModel(),
        vad=ctx.proc.userdata["vad"],
        preemptive_generation=True,
    )

    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage: {summary}")

    ctx.add_shutdown_callback(log_usage)

    await session.start(
        agent=Assistant(),
        room=ctx.room,
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
