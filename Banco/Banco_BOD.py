import sqlite3

conn = sqlite3.connect('Banco_BOD.sqlite3')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Usuario (
               id INTEGER PRIMARY KEY,
               Nro_Conta VARCHAR(10)),
               Nome VARCHAR(30),
               Email VARCHAR(30) UNIQUE,
               Senha VARCHAR(12),
               Saldo DOUBLE''')

cursor.close()
conn.commit()
print('BBDD Creada con exito!!!')

