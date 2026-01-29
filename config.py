import os
from dotenv import load_dotenv

load_dotenv()

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_CHAT_MODEL = "gemini-3-pro-preview"
GEMINI_EMBED_MODEL = "text-embedding-004"

# Retry handling
MAX_RETRIES = 2
RETRY_WAIT_SECONDS = 15

# Storage
DB_PATH = "conversations.db"
FAISS_PATH = "memory/faiss.index"

MAX_CONTEXT_MESSAGES = 6
