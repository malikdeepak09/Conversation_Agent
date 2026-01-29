# 🧠 Conversation Agent (CLI) with Contextual Memory

A **production-grade, CLI-based conversational AI agent** that remembers important facts across conversations and responds intelligently using contextual memory.

This project is designed to be:

- Easy to clone & run
- Robust in the face of API failures
- Useful even across multiple sessions

The agent uses **Gemini LLMs** for response generation, **FAISS** for semantic memory retrieval, and **SQLite** for persistent chat and memory storage.

---

## ✨ What Makes This Different?

Unlike simple chatbots, this agent:

- 🧠 **Remembers important facts** (e.g., user name)
- 🗂 **Separates short-term and long-term memory**
- 🚫 **Does NOT blindly load old chats**
- 🎯 Uses memory **only when relevant**
- 💻 Runs entirely in the **terminal (CLI)**

---

## 🚀 Key Features

### 🧠 Contextual Memory (Cross-Session)

- Important user facts are extracted and stored
- Relevant memories are retrieved using semantic similarity
- Memory persists across runs

### 🔍 FAISS Semantic Search

- Uses vector embeddings for memory retrieval
- Ensures only **relevant past context** is injected
- Prevents prompt pollution

### 💾 SQLite Persistence

- Stores:
  - Full chat history
  - Structured long-term memories
- Zero external DB setup required

### 🤖 Gemini LLM Integration

- Uses **official `google-genai` SDK**
- Graceful handling of:
  - Quota exhaustion
  - API errors
- Clean fallback messages instead of crashes

### 🖥 CLI-First UX

- No UI required
- Commands:
  - `/help`
  - `/exit`
- Designed for developers & terminal users

---

## 🛠 Technologies Used

- **Python 3.10+**
- **Gemini LLM** (via `google-genai`)
- **FAISS** (vector similarity search)
- **SQLite** (persistent storage)
- **dotenv** (environment management)

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/malikdeepak09/Conversation_Agent.git
cd Conversation_Agent
```

### 2️⃣ Create & activate a virtual environment

#### macOS / Linux

```bash
python3 -m venv myenv
source myenv/bin/activate
```

#### Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables

#### Create a .env file in the root directory:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## ▶️ Usage

#### Run the agent:

```bash
python main.py
```

#### You’ll see:

```bash
🤖 Conversation Agent (CLI)
Type /help for commands, /exit to quit
----------------------------------------

You >
```

## Contributing

If you'd like to contribute to this project, feel free to fork it and submit pull requests. Please ensure that your code follows the existing style and includes proper tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
