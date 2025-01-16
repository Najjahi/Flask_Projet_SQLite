import sqlite3

connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",('Le Petit Prince', 'Antoine de Saint-Exupéry', 'Fiction'))  
cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",('Les Misérables', 'Victor Hugo', 'Roman Historique'))  
cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",('L\'Etranger', 'Albert Camus', 'Philosophie'))  
cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",('Harry Potter à l\'école des sorciers', 'J.K. Rowling', 'Fantastique'))  
cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",('Le Seigneur des Anneaux', 'J.R.R. Tolkien', 'Fantasy'))  
cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",('Da Vinci Code', 'Dan Brown', 'Thriller'))  
cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",('L\'Art de la Guerre', 'Sun Tzu', 'Stratégie'))  
cur.execute("INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",('Les Fleurs du mal', 'Charles Baudelaire', 'Poésie'))  

connection.commit()
connection.close()
