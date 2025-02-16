import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())  #vous executer le shema

cur = connection.cursor()  #preparer l injection de lignes

cur.execute("INSERT INTO users (fname, lname, username, email, password ) VALUES (?, ?, ?)",('Imane', 'NAJJAHI', 'imane', 'imane@gmail.com', 'Cn@m2025'))
cur.execute("INSERT INTO users (fname, lname, username, email, password ) VALUES (?, ?, ?)",('Izdi', 'NAJJAHI', 'izdi', 'izdi@gmail.com', 'Cn@m2025'))
cur.execute("INSERT INTO users (fname, lname, username, email, password ) VALUES (?, ?, ?)",('Anas', 'NAJJAHI', 'anas', 'anas@gmail.com', 'Cn@m2025'))
cur.execute("INSERT INTO users (fname, lname, username, email, password ) VALUES (?, ?, ?)",('Zineb', 'ZAHIDI', 'zineb', 'zineb@gmail.com', 'Cn@m2025'))
cur.execute("INSERT INTO users (fname, lname, username, email, password ) VALUES (?, ?, ?)",('Aicha', 'ZAHIDI', 'aicha', 'aicha@gmail.com', 'Cn@m2025'))
cur.execute("INSERT INTO users (fname, lname, username, email, password ) VALUES (?, ?, ?)",('Joudia', 'ZAHIDI', 'joudia', 'joudia@gmail.com', 'Cn@m2025'))
cur.execute("INSERT INTO users (fname, lname, username, email, password ) VALUES (?, ?, ?)",('Bahija', 'ZAHIDI', 'bahija', 'bahija@gmail.com', 'Cn@m2025'))
cur.execute("INSERT INTO users (fname, lname, username, email, password ) VALUES (?, ?, ?)",('Amina', 'ZAHIDI', 'amina', 'amina@gmail.com', 'Cn@m2025'))

connection.commit()
connection.close()
