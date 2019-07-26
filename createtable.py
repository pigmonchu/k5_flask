import sqlite3

conn = sqlite3.connect('movimientos.db')

cursor = conn.cursor()

query = '''
    CREATE TABLE "movimientos" (
        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
        "fecha"	TEXT NOT NULL,
        "concepto"	TEXT,
        "monedaComprada"	TEXT NOT NULL,
        "cantidadComprada"	REAL NOT NULL,
        "monedaPagada"	TEXT NOT NULL,
        "cantidadPagada"	REAL NOT NULL
    );
'''

rows = cursor.execute(query)



