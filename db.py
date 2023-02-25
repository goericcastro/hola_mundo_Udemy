import mysql.connector

midb = mysql.connector.connect(
    host = 'localhost',
    user = 'ericc',
    password = 'mysql2022',
    database = 'prueba'
)

cursor = midb.cursor()

cursor.execute('select * from usuario')

resultado = cursor.fetchall()

print(resultado)