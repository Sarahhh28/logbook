import sqlite3

def init_db():
    conn = sqlite3.connect('logbuch.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logbuch
                     (id INTEGER PRIMARY KEY, eintrag TEXT)''')
    conn.commit()
    conn.close()

def add_entry(eintrag):
    conn = sqlite3.connect('logbuch.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logbuch (eintrag) VALUES (?)", (eintrag,))
    conn.commit()
    conn.close()

def get_entries():
    conn = sqlite3.connect('logbuch.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logbuch")
    rows = cursor.fetchall()
    conn.close()
    return rows