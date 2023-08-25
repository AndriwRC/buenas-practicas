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

cursor.close
conn.close