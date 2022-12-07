import sqlite3 as sq

db = "db.sqlite3"

def get_pid():
    conn = sq.connect(db)
    cursor = conn.cursor()
    highest_pid = cursor.execute("SELECT pid FROM ChatSite_privateroom ORDER BY pid DESC").fetchone()
    if highest_pid == None:
        return 1
    highest_pid = highest_pid[0]
    return highest_pid + 1

def get_user_rooms(user):
    conn = sq.connect(db)
    cursor = conn.cursor()
    query = cursor.execute(f"SELECT pid FROM ChatSite_privateroom WHERE member1='{str(user)}' OR member2='{str(user)}'").fetchall()
    if query == None:
        return None
    rooms = []
    for room in query:
        rooms.append(room[0])
    return rooms

def search_messages_query(user_input, room):
    conn = sq.connect(db)
    cursor = conn.cursor()

    messages = []
    #results = cursor.execute(f"SELECT user, pub_date, content FROM ChatSite_message WHERE room_nr={room} AND content LIKE '%{user_input}%'")
    results = cursor.execute("""SELECT user, pub_date, content FROM ChatSite_message WHERE room_nr= ? AND content= ?""", (room,str(user_input)))
    for res in results:
        messages.append(f"{res[0]} [{res[1][11:16]}]: {res[2]}")
    return messages
