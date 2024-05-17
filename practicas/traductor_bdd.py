'''Perfeccionar el ejercicio de traductor implementando base de datos mysql
crear  una tabla llamada traductor  con los campos: id, español, ingles'''

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_traductor_python"
)

cursor=mydb.cursor()

palabra=input("ingrese la palabra a traducir: ")
sentencia=f"select ingles from traductor where español like'{palabra}'"
cursor.execute(sentencia)

resultado=cursor.fetchall()

# si existe imprimir, sino solicitar para agregar un nueva palabra

for x in resultado:
    print(x)