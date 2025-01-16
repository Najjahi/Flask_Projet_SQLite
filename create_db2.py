import sqlite3

connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())  #vous executer le shema

cur = connection.cursor()  #preparer l injection de lignes

Le Petit Prince	Antoine de Saint-Exupéry	Fiction
3	Les Misérables	Victor Hugo	Roman Historique
4	L'Étranger	Albert Camus	Philosophie
5	Harry Potter à l'école des sorciers	J.K. Rowling	Fantastique
6	Le Seigneur des Anneaux	J.R.R. Tolkien	Fantasy
7	Da Vinci Code	Dan Brown	Thriller
8	L'Art de la Guerre	Sun Tzu	Stratégie
9	La Peste	Albert Camus	Roman
10	Les Fleurs du mal	Charles Baudelaire	Poésie
connection.commit()
connection.close()
