# Jarvis V1

Full voice AI agent: Ears (Whisper) -> Memory (persistent) -> Brain (LLM + Tools + RAG) -> Mouth (Orpheus).

## Setup

1. `pip install -r requirements.txt`
2. Rename `.env.example` to `.env`, add your real `GROQ_API_KEY`
3. Edit `notes.txt` with real facts about Jarvis/yourself for RAG to search
4. `python main.py`

## Architecture

- `config.py` - shared client + model names, single source of truth
- `memory.py` - conversation saved to `memory.json`, survives restarts
- `tools.py` - real functions (calculate, search_notes) + their schemas
- `rag.py` - embeds `notes.txt`, exposed to the model as the `search_notes` tool
- `voice.py` - record/transcribe/speak
- `main.py` - the loop tying it together

## Key design decision

Tools and RAG are both exposed to the model as callable functions in one
`tools` list - the model decides per-question whether it needs math,
notes, or neither. This is the actual production pattern: one decision
point, not hardcoded "always check RAG first" logic.

## Known limits / next upgrades

- Fixed 5-second recording window (no silence detection yet)
- Chat responses can occasionally hit the TTS free-tier token limit on long
  answers - system prompt already constrains to 2-3 sentences
- `notes.txt` uses one-line-per-chunk; upgrade to real paragraph chunking
  once notes grow past a page
- Memory grows unbounded in `memory.json` - add summarization/trimming
  once conversations get long (same cost/speed tradeoff discussed in
  Week 14 memory lessons)
