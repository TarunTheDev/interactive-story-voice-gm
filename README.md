# 🎲 Voice Game Master - AI Dungeon Master for D&D Adventures

Ever wanted a personal Dungeon Master who's available 24/7? One who never forgets your backstory, crafts immersive worlds on the fly, and responds to your wildest decisions without skipping a beat?

**Meet the Voice Game Master** - an AI-powered D&D-style adventure companion that brings tabletop roleplaying to life through voice interaction.

![Voice Game Master Demo](https://img.shields.io/badge/Status-Live-brightgreen) ![Built with LiveKit](https://img.shields.io/badge/Built%20with-LiveKit-blue) ![Murf Falcon TTS](https://img.shields.io/badge/TTS-Murf%20Falcon-purple)

---

## What is This?

This is a voice-controlled Game Master that runs interactive fantasy adventures in real-time. Think of it as having a skilled storyteller in your pocket who:

- **Paints vivid scenes** - Every location comes alive with rich sensory details
- **Remembers everything** - Your past choices shape future encounters
- **Improvises brilliantly** - No matter what you decide, the story adapts
- **Voices unique characters** - Each NPC has their own personality and speaking style

Built for the **Murf AI Voice Agent Challenge**, this project showcases what's possible when you combine cutting-edge voice AI with the timeless magic of tabletop roleplaying.

---

## The Tech Behind the Magic

| Component | Technology | Purpose |
|-----------|------------|---------|
| 🎤 Speech Recognition | Deepgram Nova-3 | Converts your voice to text with incredible accuracy |
| 🧠 Game Master Brain | Google Gemini 2.5 Flash | Powers the storytelling, NPC dialogue, and world-building |
| 🔊 Voice Output | Murf Falcon TTS | Brings the Game Master to life with natural, expressive speech |
| 🔄 Real-time Comms | LiveKit | Handles the WebRTC magic for seamless voice interaction |

---

## Getting Started

### You'll Need

- Python 3.9 or higher
- Node.js 18+ with pnpm
- A microphone and speakers (or headphones)
- API keys for Deepgram, Google AI, and Murf

### Quick Setup

**1. Clone and enter the project:**
```bash
git clone https://github.com/yourusername/voice-game-master.git
cd voice-game-master
```

**2. Set up the backend:**
```bash
cd backend
pip install -e .
cp .env.example .env.local
```

Edit `.env.local` with your API keys:
```
LIVEKIT_URL=ws://127.0.0.1:7880
LIVEKIT_API_KEY=devkey
LIVEKIT_API_SECRET=secret
GOOGLE_API_KEY=your_google_api_key
MURF_API_KEY=your_murf_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key
```

**3. Set up the frontend:**
```bash
cd ../frontend
pnpm install
cp .env.example .env.local
```

Add the same LiveKit credentials to `frontend/.env.local`.

**4. Launch the adventure:**

Open three terminal windows:

```bash
# Terminal 1 - Start LiveKit Server
./livekit-server.exe --dev   # Windows
# or: livekit-server --dev   # Mac/Linux

# Terminal 2 - Start the Game Master
cd backend
python src/agent.py dev

# Terminal 3 - Start the web interface
cd frontend
pnpm dev
```

**5. Open your browser to `http://localhost:3000` and start playing!**

---

## Your First Adventure

When you connect, the Game Master welcomes you to the **Crossroads Inn** in Millbrook village. A mysterious hooded figure has been asking about adventurers brave enough to investigate strange happenings in the **Whispering Woods**.

From there, it's your story. Will you:
- Approach the mysterious stranger?
- Gather supplies and information from the villagers?
- Head straight into the woods alone?

Every choice matters. Every decision shapes the narrative.

---

## Sample Conversation

> **Game Master:** "Welcome, adventurer, to the mystical realm of Eldoria! You find yourself pushing open the heavy oak door of the Crossroads Inn. The warmth washes over you, carrying scents of roasted boar and woodsmoke. In a shadowed corner, a hooded figure sits alone, watching you with keen interest. What do you do?"

> **You:** "I want to approach the hooded figure and ask about the Whispering Woods."

> **Game Master:** "A bold choice! As you draw closer, the air grows noticeably cooler. From beneath the hood, a gravelly voice emerges: 'So, another brave soul seeks the truth? The Woods are not as they once were. A darkness stirs there.' The figure gestures to an empty seat. 'Take a seat, if you wish to truly hear what troubles Eldoria's ancient heart.' Do you sit, or do you have questions first?"

---

## Project Structure

```
voice-game-master/
├── backend/
│   ├── src/
│   │   └── agent.py      # The Game Master's brain
│   └── .env.local        # Your API keys (keep secret!)
├── frontend/
│   ├── app/              # Next.js web interface
│   └── components/       # React components
└── livekit-server.exe    # Local development server
```

---

## Why I Built This

I've been playing D&D for years, but finding a group that can meet regularly is tough. And while solo RPG adventures exist, they never quite captured that feeling of having a real Game Master respond to your choices.

When I discovered the Murf AI Voice Agent Challenge, I knew exactly what I wanted to build. Voice is the perfect medium for storytelling - it's intimate, it's immersive, and it brings characters to life in a way that text simply can't.

The result is something I'm genuinely proud of: a Game Master who's always ready to run an adventure, who never gets tired of your wild ideas, and who can weave a story as unique as the player experiencing it.

---

## What's Next?

This is just the beginning. Future plans include:

- **Character sheets** - Track your stats, inventory, and abilities
- **Dice rolling** - Add actual game mechanics for combat and skill checks
- **Save/load games** - Continue your adventures across sessions
- **Multiple worlds** - Switch between fantasy, sci-fi, horror, and more

---

## Built With ❤️ For

**Murf AI Voice Agent Challenge** - Showcasing the power of Murf Falcon, the fastest TTS API available.

---

## Credits

- [LiveKit](https://livekit.io/) for the incredible real-time communication framework
- [Murf AI](https://murf.ai/) for Falcon TTS that makes the Game Master sound amazing
- [Deepgram](https://deepgram.com/) for speech recognition that actually understands you
- [Google](https://ai.google/) for Gemini, the LLM that powers the storytelling

---

## License

MIT License - Feel free to fork, modify, and create your own adventures!

---

*Roll for initiative. Your adventure awaits.*
