'''Implementar un traductor de palabras del español a inglés usando la estructura
de diccionario. 
Debe solicitar una palabra al usuario y verificar si existe en el diccionario y 
mostrar la traducción.
En caso de no existir la palabra en el diccionario, solicitar si desea agregar al diccionario.
El diccionario se detiene al introducir 0'''

traductor={
    "perro":"dog",
    "gato":"cat",
    "casa":"house"
}

'''
while True:
    palabra=input("ingrese la palabra a traducir: ")
    if palabra in traductor:
        print(f"{palabra} en ingles es: ",traductor[palabra])
    else:
        print(f"{palabra} no se encuentra en el traductor")
    opcion=input("desea ingresar la palabra al tructor?, si o no: ")
    if opcion=="si":
        palabra_nueva=input("ingrese la palabra: ")
        traduccion=input("ingrese la traduccion: ")
        traductor[palabra_nueva]=traduccion
        print("palabra agregada...")
    else:
        print("no se agrego palabra")
    salir=int(input("ingrese cero para salir o otro numero para continuar: "))
    if salir==0:
        break'''
        
while True:
    palabra=input("ingrese la palabra a traducir o cero para salir:")
    if palabra in traductor:
        print(f"{palabra} en ingles es: ",traductor[palabra])
    elif palabra=="0":
        break
    else:
        print("la palabra no esta en el traductor")
        opcion=input("desa traducir si o no: ")
        if opcion=="si":
            palabra_nueva=input("ingrese la palabra:")
            traduccion=input("ingrese la traduccion: ")
            traductor[palabra_nueva]=traduccion
            print("se agrego al traductor")
        else:
            print("no se agrego al traductor")

print(traductor)