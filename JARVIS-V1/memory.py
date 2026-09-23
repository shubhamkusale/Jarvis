"""
Persistent memory: same idea as your Week 14 conversation list,
but saved to a JSON file so it survives closing the script -
this is the real fix to the "restart = forgets everything" limitation
you asked about back in Week 14.
"""
import json
import os

MEMORY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "memory.json")

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are Jarvis, a helpful voice-based AI assistant. "
        "Keep answers to 2-3 sentences max since responses are spoken aloud. "
        "Use tools when the question needs real calculation or requires searching "
        "the user's personal notes."
    )
}

