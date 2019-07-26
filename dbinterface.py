import sqlite3

conn = sqlite3.connect('movimientos.db')
cursor = conn.cursor()

def insert(fecha, concepto, monedaComprada, cantidadComprada, monedaPagada, cantidadPagada):
    print('insert')

    query = ''' 
    INSERT INTO movimientos 
    (fecha, concepto, monedaComprada, cantidadComprada, monedaPagada, cantidadPagada)
    values (?, ?, ?, ?, ?, ?);
    '''
    rows = cursor.execute(query, 
    (fecha, concepto, monedaComprada, cantidadComprada, monedaPagada, cantidadPagada))
    conn.commit()

def updateConcepto(id, concept):
    query = '''
    UPDATE movimientos 
       SET concepto = ?
     WHERE id = ?;
    '''
    rows = cursor.execute(query, (concept, id))
    conn.commit()

def selectMovement(fecha, monedaComprada):
    query = '''
    SELECT * FROM movimientos WHERE fecha < ? and monedaComprada = ?;
    '''
    rows = cursor.execute(query, (fecha, monedaComprada))
    for row in rows:
        print(row)



selectMovement('2018-12-31', 'EUR')
