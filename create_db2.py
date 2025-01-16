import sqlite3

connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())  #vous executer le shema

cur = connection.cursor()  #preparer l injection de lignes

cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('Les Miserables', 'Victor Hugo', 'Roman Historique'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('Le Petit Prince', 'Antoine de Saint-Exupéry', 'Fiction'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('Le Seigneur des Anneaux', 'J.R.R. Tolkien', '789, Fantasy'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('Da Vinci Code', 'Dan Brown', 'Thriller'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('La Peste', 'Albert Camus', 'Roman'))
cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('Les Fleurs du mal', 'Charles Baudelaire', 'Poesie'))
#cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'))
#cur.execute("INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)",('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris'))


connection.commit()
connection.close()
