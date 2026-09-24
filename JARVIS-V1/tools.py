"""
Real functions the model can request, plus the JSON schema descriptions
it reads to decide when to use them. RAG search is exposed as a tool too -
this is the actual professional pattern: instead of hardcoding
"always run RAG first, then check tools," you hand the model both
capabilities and let it decide per-question, exactly like it already
decides between calculate() and answering directly.
"""
from rag import search_notes


def calculate(expression: str) -> str:
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluates a math expression and returns the exact result.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "A math expression like '847 * 392'"}
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_notes",
            "description": "Searches Jarvis's personal notes/knowledge base for relevant information about Jarvis itself, its architecture, or facts the user has stored.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "What to search for in the notes"}
                },
                "required": ["query"]
            }
        }
    }
]

# Maps a tool's name (as the model requests it) to the real Python function
TOOL_DISPATCH = {
    "calculate": calculate,
    "search_notes": search_notes
}
