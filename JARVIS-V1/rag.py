"""
RAG, same mechanism you already built (embed -> cosine similarity -> best match),
wrapped as a callable function instead of a standalone script. This version
reads from notes.txt so you can put your real Jarvis notes there.
"""
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from config import EMBED_MODEL

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_FILE = os.path.join(BASE_DIR, "notes.txt")

_embedder = SentenceTransformer(EMBED_MODEL)

with open(NOTES_FILE, "r") as f:
    # one chunk per non-empty line - swap for real chunking later if notes grow
    DOCUMENTS = [line.strip() for line in f if line.strip()]

_doc_embeddings = _embedder.encode(DOCUMENTS)


def search_notes(query: str, top_k: int = 1) -> str:
    """Search Jarvis's notes for the most relevant chunk(s) to a query."""
    query_embedding = _embedder.encode([query])
    similarities = cosine_similarity(query_embedding, _doc_embeddings)[0]
    top_indices = np.argsort(similarities)[::-1][:top_k]
    matches = [DOCUMENTS[i] for i in top_indices]
    return " ".join(matches)
