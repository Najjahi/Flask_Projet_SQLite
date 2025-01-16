import sqlite3

connection = sqlite3.connect('database2.db')

with open('schema2.sql') as f:
    connection.executescript(f.read())  #vous executer le shema

cur = connection.cursor()  #preparer l injection de lignes



connection.commit()
connection.close()
