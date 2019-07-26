import sqlite3

conn = sqlite3.connect('movimientos.db')

cursor = conn.cursor()

rows = cursor.execute('select * from movimientos;')

for row in rows:
	print(row)

	



