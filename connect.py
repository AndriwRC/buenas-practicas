import sys
import pyodbc
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\cuc\Documents\RegistroNotas\bdprueba.accdb;")
cursor=conn.cursor()

datos_persona = [
    {"Nombre": "Alice", "Apellido": "Johnson", "Edad": 25},
    {"Nombre": "Bob", "Apellido": "Smith", "Edad": 32},
    {"Nombre": "Charlie", "Apellido": "Brown", "Edad": 28},
    {"Nombre": "David", "Apellido": "Davis", "Edad": 40},
    {"Nombre": "Eve", "Apellido": "Taylor", "Edad": 22}
]

for persona in datos_persona:
    query = "INSERT INTO persona1 (Nombre, Apellido, Edad) VALUES (?, ?, ?)"
    cursor.execute(query, (persona["Nombre"], persona["Apellido"], persona["Edad"]))
    conn.commit()

# Consultas

print("Consulta para obtener todos los registros:")
cursor.execute("SELECT * FROM persona1")
for row in cursor.fetchall():
    print(row)


print("Consulta para obtener registros con cierta edad:")
cursor.execute("SELECT * FROM persona1 WHERE Edad >= ?", (30,))
for row in cursor.fetchall():
    print(row)

print("Consulta para obtener registros ordenados por edad:")
cursor.execute("SELECT * FROM persona1 ORDER BY Edad")
for row in cursor.fetchall():
    print(row)

print("Consulta para obtener el número total de registros:")
cursor.execute("SELECT COUNT(*) FROM persona1")
count = cursor.fetchone()[0]
print("Número total de registros:", count)

cursor.close
conn.close