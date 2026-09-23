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


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return [SYSTEM_PROMPT]


def save_memory(conversation):
    with open(MEMORY_FILE, "w") as f:
        json.dump(conversation, f, indent=2)


def add_message(conversation, role, content, tool_call_id=None, tool_calls=None):
    msg = {"role": role, "content": content}
    if tool_call_id:
        msg["tool_call_id"] = tool_call_id
    if tool_calls:
        msg["tool_calls"] = tool_calls
    conversation.append(msg)
    return conversation
