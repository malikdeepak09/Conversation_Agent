import re
from llm.embeddings import EmbeddingClient
from memory.faiss_store import FAISSStore
from db.chat_repository import ChatRepository

class MemoryManager:
    def __init__(self):
        self.embedder = EmbeddingClient()
        self.store = FAISSStore()
        self.repo = ChatRepository()
        self.repo.init_memory_table()

    def _extract_fact(self, user_text: str):
        """
        Very basic fact extraction.
        We will improve this later using LLMs.
        """
        user_text = user_text.lower()

        # Name extraction
        match = re.search(r"my name is (\w+)", user_text)
        if match:
            return f"User's name is {match.group(1).capitalize()}"

        return None

    def maybe_store_memory(self, user, assistant):
        fact = self._extract_fact(user)
        if not fact:
            return  # nothing worth remembering

        vector = self.embedder.embed(fact)
        self.repo.save_memory(fact)
        self.store.add(vector)

    def retrieve_relevant(self, query):
        if self.store.is_empty():
            return []

        vector = self.embedder.embed(query)
        _, idxs = self.store.search(vector)

        memories = []
        for idx in idxs:
            content = self.repo.get_memory_by_index(idx)
            if content:
                memories.append(content)

        return memories
