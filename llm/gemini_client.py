import time
from google import genai
from google.genai.errors import ClientError
from config import (
    GEMINI_API_KEY,
    GEMINI_CHAT_MODEL,
    MAX_RETRIES,
    RETRY_WAIT_SECONDS
)
from prompts.prompt_loader import load_prompt

SYSTEM_PROMPT = load_prompt("system.txt")
MEMORY_PROMPT = load_prompt("memory.txt")


class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_response(self, user_input, memories, recent_messages):
        history = "\n".join(
            [f"{role}: {msg}" for role, msg in recent_messages]
        )

        memory_block = ""
        if memories:
            memory_block = MEMORY_PROMPT.format(
                memories="\n".join(memories)
            )

        prompt = f"""
{SYSTEM_PROMPT}

{memory_block}

Conversation:
{history}

User: {user_input}
Assistant:
"""

        for attempt in range(MAX_RETRIES + 1):
            try:
                response = self.client.models.generate_content(
                    model=GEMINI_CHAT_MODEL,
                    contents=prompt
                )
                return response.text.strip()

            except ClientError as e:
                error_text = str(e).lower()

                if "resource_exhausted" in error_text or "quota" in error_text:
                    if attempt < MAX_RETRIES:
                        print(
                            f"\n⚠️ Gemini quota hit. Retrying in "
                            f"{RETRY_WAIT_SECONDS}s..."
                        )
                        time.sleep(RETRY_WAIT_SECONDS)
                        continue

                    return (
                        "⚠️ Gemini API quota exceeded.\n"
                        "Please enable billing or try again later."
                    )

                return (
                    "❌ Gemini API error occurred.\n"
                    "Please try again later."
                )

            except Exception as e:
                return f"❌ Unexpected LLM error: {e}"
