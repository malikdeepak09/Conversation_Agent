import uuid
from db.sqlite_store import get_connection

class ChatRepository:
    def __init__(self):
        self._init_chat_table()

    def _init_chat_table(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS chats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                role TEXT,
                message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

    def init_memory_table(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT
            )
        """)
        conn.commit()
        conn.close()

    def create_new_session(self):
        return str(uuid.uuid4())

    def save_message(self, session_id, role, message):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO chats (session_id, role, message) VALUES (?, ?, ?)",
            (session_id, role, message)
        )
        conn.commit()
        conn.close()

    def get_recent_messages(self, session_id, limit=6):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT role, message FROM chats
            WHERE session_id=?
            ORDER BY id DESC LIMIT ?
        """, (session_id, limit))
        rows = cur.fetchall()
        conn.close()
        return list(reversed(rows))

    def save_memory(self, content):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO memories (content) VALUES (?)",
            (content,)
        )
        conn.commit()
        conn.close()

    def get_memory_by_index(self, idx):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT content FROM memories WHERE id = ?",
            (idx + 1,)
        )
        row = cur.fetchone()
        conn.close()
        return row[0] if row else None
