class Router:
    def is_followup(self, query: str) -> bool:
        keywords = ["previous", "earlier", "before", "last time"]
        return any(k in query.lower() for k in keywords)
