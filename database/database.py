import sqlite3
import os
from datetime import datetime

# Use /tmp on Vercel to avoid Read-Only File System errors (though data won't persist long-term)
if os.environ.get('VERCEL'):
    DB_FILE = '/tmp/meal_history.db'
else:
    DB_FILE = 'database/meal_history.db'

def init_db():
    os.makedirs(os.path.dirname(DB_FILE) or '.', exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            detected_category TEXT,
            diet_preference TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def save_query(user_input, detected_category, diet_preference=""):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute(
        "INSERT INTO history (user_input, detected_category, diet_preference, timestamp) VALUES (?, ?, ?, ?)",
        (user_input, detected_category, diet_preference, timestamp)
    )
    
    conn.commit()
    conn.close()

def get_recent_history(limit=10):
    if not os.path.exists(DB_FILE):
        return []
        
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT user_input, detected_category, diet_preference, timestamp FROM history ORDER BY timestamp DESC LIMIT ?", 
        (limit,)
    )
    
    rows = cursor.fetchall()
    conn.close()
    
    history = []
    for row in rows:
        history.append({
            "user_input": row[0],
            "detected_category": row[1],
            "diet_preference": row[2],
            "timestamp": row[3]
        })
        
    return history
