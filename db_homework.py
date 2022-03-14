from multiprocessing import connection
import sqlite3

connection = sqlite3.connect("homework.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXIST users (username, password)")
connection.commit()
connection.close()