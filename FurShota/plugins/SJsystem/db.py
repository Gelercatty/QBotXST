import sqlite3
from typing import List, Optional, Dict

class SJDB:
    def __init__(self, db_name: str = "messages.db"):
        self.db_name = db_name
        self._init_db()

    # 初始化数据库和表
    def _init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    SJ_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender_id INTEGER NOT NULL,
                    message_id INTEGER NOT NULL
                )
            """)
            conn.commit()

    # 插入一条记录
    def insert_SJ(self, sender_id: int, message_id: int):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO messages (sender_id, message_id) VALUES (?, ?)", (sender_id, message_id))
            conn.commit()

    # 按 SJ_id 获取记录
    def get_SJ_sjid(self, SJ_id: int) -> Optional[Dict[str, int]]:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM messages WHERE SJ_id = ?", (SJ_id,))
            result = cursor.fetchone()
            
            if result:
                return {"SJ_id": result[0], "sender_id": result[1], "message_id": result[2]}
            else:
                return None

    # 按 sender_id 获取所有记录
    def get_SJ_senderid(self, sender_id: int) -> List[Dict[str, int]]:
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM messages WHERE sender_id = ?", (sender_id,))
            results = cursor.fetchall()
            
            return [{"SJ_id": row[0], "sender_id": row[1], "message_id": row[2]} for row in results] if results else []

# 用法示例
if __name__ == "__main__":
    db = MessageDB()
    db.insert_SJ(12345, 67890)
    print(db.get_SJ_sjid(1))
    print(db.get_SJ_senderid(12345))
