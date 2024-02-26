import sqlite3
import hashlib

conn = sqlite3.connect("userdata2.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata2 (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "mike213", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "john1313", hashlib.sha256("mynameis".encode()).hexdigest()
username3, password3 = "petko3", hashlib.sha256("vratarqtt23".encode()).hexdigest()
username4, password4 = "slavi3213", hashlib.sha256("kikboksorut".encode()).hexdigest()

cur.execute("INSERT INTO userdata2 (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata2 (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata2 (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata2 (username, password) VALUES (?, ?)", (username4, password4))
print(f"username: {username1}")
print(f"password: {password1}")
print(f"password: {password1}")

conn.commit()
