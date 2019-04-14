import db
import threading
import time

def create_user(username):
    conn = db.get_connection()

    c = conn.cursor()
    c.execute('INSERT INTO users (username) VALUES (?)', (username,))

    conn.commit()
    conn.close()

def get_user(username):
    conn = db.get_connection()

    c = conn.cursor()
    c.execute("SELECT * from users where username = ?", (username,) ) 

    user = c.fetchone()['username']
    conn.close()
    return user

def get_players():
    all_players = []

    conn = db.get_connection()

    c = conn.cursor()
    c.execute("SELECT * FROM users")
    result = c.fetchall()
    for i in result:
        all_players.append(i["username"])
        
    conn.close()
    return all_players

def remove_player(username):
    conn = db.get_connection()

    c = conn.cursor()
    c.execute("SELECT * from users where username = ?", (username,) ) 
    user = c.fetchone()['username']
    c.execute("DELETE FROM users where username = ?", (username,) )

    conn.commit()
    conn.close()
    return user

def countdown():
    n = 10
    while n > 0:
        n = n - 1
        return n
    if n == 0:
        return n
  
