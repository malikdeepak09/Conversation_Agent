def handle_command(cmd: str) -> bool:
    if cmd == "/exit":
        print("👋 Goodbye!")
        return True

    if cmd == "/help":
        print("""
Available commands:
/help   Show this help
/exit   Exit the agent
""")
    return False
