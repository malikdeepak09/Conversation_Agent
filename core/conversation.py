from llm.gemini_client import GeminiClient
from db.chat_repository import ChatRepository
from memory.memory_manager import MemoryManager
from core.commands import handle_command


class Conversation:
    def __init__(self):
        # Initialize persistence + session
        self.repo = ChatRepository()
        self.session_id = self.repo.create_new_session()

        # Initialize LLM + memory
        self.llm = GeminiClient()
        self.memory = MemoryManager()

    def start(self):
        while True:
            user_input = input("\nYou > ").strip()

            # Handle CLI commands
            if user_input.startswith("/"):
                if handle_command(user_input):
                    break
                continue

            # Save user message
            self.repo.save_message(self.session_id, "user", user_input)

            try:
                # Retrieve only relevant long-term memories
                memories = self.memory.retrieve_relevant(user_input)

                # Generate LLM response
                response = self.llm.generate_response(
                    user_input=user_input,
                    memories=memories,
                    recent_messages=self.repo.get_recent_messages(
                        self.session_id
                    )
                )

                # Print + persist assistant response
                print(f"\nAgent > {response}")
                self.repo.save_message(
                    self.session_id, "assistant", response
                )

                # Store memory (best-effort, never fatal)
                try:
                    self.memory.maybe_store_memory(
                        user_input, response
                    )
                except Exception as mem_err:
                    print(
                        "⚠️ Memory storage skipped:",
                        repr(mem_err)
                    )

            except Exception as e:
                # Absolutely nothing should crash the CLI loop
                print("\n❌ Error occurred:")
                print(repr(e))
