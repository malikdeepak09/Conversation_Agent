from core.conversation import Conversation

def main():
    print("\n🤖 Conversation Agent (CLI)")
    print("Type /help for commands, /exit to quit")
    print("-" * 40)

    convo = Conversation()
    convo.start()

if __name__ == "__main__":
    main()
