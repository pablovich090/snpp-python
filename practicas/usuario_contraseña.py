'''while i<4:
    user=input("ingrese el ususario: ")
    clave=int(input("ingrese la contraseña: "))
    if user=="palo" and clave==123:
        print("acceso otorgado")
        break
    elif i==3:
        print("acceso denegado")
    else:
        print("intente de nuevo")
    i=i+1'''



'''Escriba un programa para validar si los datos de acceso (usuario y contraseña) se encuentran
en el diccionario.
Validar a solo 3 intentos erroneos de contraseña utilizando ciclo while.'''

dato_acceso={
    "admin":"123",
    "palo":"321",
    "raul":"789",
}


i=1;
 
while i<4:
    user=input("ingrese el usuario: ")
    clave=input("ingrese la contraseña: ")
    if user in dato_acceso and clave in dato_acceso[user]:
        print("acceso otorgado")
        break
    elif i==3:
        print("acceso denegado")
    else:
        print("intente de nuevo")
    i=i+1
 
     
