"""
Jarvis V1 - full loop: Ears -> Memory -> Brain (+Tools+RAG) -> Mouth.

Run this, speak, and it listens, thinks (using tools/notes if needed),
remembers the conversation across restarts, and speaks back.
"""
import json
from config import client, CHAT_MODEL
from memory import load_memory, save_memory, add_message
from tools import TOOLS_SCHEMA, TOOL_DISPATCH
from voice import record_audio, transcribe_audio, speak
from utils import call_with_retry

def get_response(conversation):
    response = call_with_retry(
        client.chat.completions.create,
        model=CHAT_MODEL,
        messages=conversation,
        tools=TOOLS_SCHEMA
    )
    reply = response.choices[0].message


def get_response(conversation):
    """
    Sends the conversation to the model with tools available.
    If the model requests a tool, runs it and calls again for the
    real final answer - same round-trip pattern from Week 14 Block 4,
    just looped in case the model chains multiple tool calls.
    """
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=conversation,
        tools=TOOLS_SCHEMA
    )
    reply = response.choices[0].message

    if reply.tool_calls:
        # Record the model's own tool request in the conversation
        conversation.append({
            "role": "assistant",
            "content": reply.content or "",
            "tool_calls": [tc.model_dump() for tc in reply.tool_calls]
        })

        for tool_call in reply.tool_calls:
            func_name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            result = TOOL_DISPATCH[func_name](**args)

            conversation.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

        # Call again now that real tool results are in the conversation
        return get_response(conversation)

    return reply.content


def main():
    conversation = load_memory()
    print("Jarvis V1 - press Ctrl+C to stop")

    while True:
        record_audio(duration=5)
        spoken_text = transcribe_audio()
        print("You said:", spoken_text)

        conversation = add_message(conversation, "user", spoken_text)

        answer = get_response(conversation)
        print("Jarvis says:", answer)

        conversation = add_message(conversation, "assistant", answer)
        save_memory(conversation)

        speak(answer)


if __name__ == "__main__":
    main()
