import sqlite3
import os

db_file = "rx.db"

def db_exists():
    if os.path.exists(db_file):
        return True
    else:
        return False

# not used
def db_create():
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

# not used
def read_conf():
    conn = None 
    res = {}
    try:
        # connect to db
        conn = sqlite3.connect(db_file)
        # get cursor
        cursor = conn.cursor()
        # Create table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS conf (
            name TEXT PRIMARY KEY, 
            value TEXT)''')
        # Get Record
        cursor.execute("SELECT name, value from conf")
        # fetch the records
        rows = cursor.fetchall() 
        # loop through rows
        for row in rows:
            n = row[0]
            v = row[1]
            # add the name-value to res
            res[n] = v
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        # return value
        return res

def upd_hftoken(token):
    conn = None
    ret = True
    try:
        # connect to db
        conn = sqlite3.connect(db_file)
        # get cursor
        cursor = conn.cursor()
        # Create table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS conf (
                    name TEXT PRIMARY KEY, 
                    value TEXT)''')
        # Upsert Record
        cursor.execute("INSERT INTO conf (name, value) VALUES (:name, :value) ON CONFLICT (name) DO UPDATE SET value = :value", {"name": "hftoken", "value": token})
        #cursor.execute("INSERT INTO conf (name, value) VALUES ('hftoken', 'Hello')")
        conn.commit()
    except sqlite3.Error as e:
        print(e)
        ret = False
    finally:
        if conn:
            conn.close()
        return {"success": ret }