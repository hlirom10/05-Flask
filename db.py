import sqlite3

conn = sqlite3.connect("database.db")         # lager eller åpner databasen
print("opened db with sucess")

conn.execute("CREATE TABLE IF NOT EXISTS login (username TEXT, pwd TEXT)")         # lager tabellen login
print("table created sucessfully")

conn.close()         # lukker databasen