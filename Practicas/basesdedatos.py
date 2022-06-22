import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()

usuarios = [
    ('nefftep79@gmail.com', 'Software', 'Marco', 24),
    ('Mariamvelasquez27@gmail.com', 'Diseño', 'Mariam', 22)
]

cursor.executemany("INSERT INTO estudiantes VALUES (?,?)", usuarios)
conexion.commit()

cursor.execute('SELECT * FROM estudiantes')
usuarios = cursor.fetchall()

for u in usuarios:
    print(u)
conexion.close()