from google import genai
from config import GEMINI_API_KEY, GEMINI_EMBED_MODEL

class EmbeddingClient:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def embed(self, text: str):
        result = self.client.models.embed_content(
            model=GEMINI_EMBED_MODEL,
            contents=text
        )
        return result.embeddings[0].values
