# queremos leer la tabla de monedas y que nos devuelva un array de tuplas (symbo, name) como este
# [('EUR', 'Euros'), ('BTC', 'Bitcoins'), ('LTC', 'Litecoins'), ('ETH', 'Ethereum')]

import sqlite3

conn = sqlite3.connect('data/movimientos.db')
cursor = conn.cursor()

def consultaMonedas():
    query = '''
            SELECT symbol, name FROM monedas;
            '''

    rows = cursor.execute(query) #Luis se va a la fruteria y deja las patatas en rows

    resp = []
    for row in rows:
        resp.append(row)

    conn.close()
    return resp

def diccMonedas():
    query = '''
            SELECT id, symbol FROM monedas;
            '''
    rows = cursor.execute(query)
    resp = {}
    for row in rows:
        resp[row[0]] = row[1]
    print(resp)
    conn.close()
    return resp

diccMonedas()