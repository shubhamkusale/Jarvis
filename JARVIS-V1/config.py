"""
Central config: loads env, creates the one shared Groq client.
Every other module imports `client` from here instead of creating its own.
"""
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

CHAT_MODEL = "openai/gpt-oss-120b"
STT_MODEL = "whisper-large-v3"
TTS_MODEL = "canopylabs/orpheus-v1-english"
TTS_VOICE = "troy"
EMBED_MODEL = "all-MiniLM-L6-v2"
