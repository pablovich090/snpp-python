'''Leer tres notas por teclado y cargarlos en una lista.
Validar que las notas estén en el rango de 1 a 5.
Calcular el promedio y si está aprobado o reprobado.
Si el promedio es mayor a 1.7 entonces aprobado sino reprobado'''


notas=[]
#leer datos

for x in range(1,4):
    # validar que las notas sean del 1 al 5
    nota=int(input(f"ingrese la nota {x}: "))
    while nota<1 or nota>5:
        nota=int(input("error al ingresar la nota...vualva a ingresar: "))
    notas.append(nota)



print("las notas son: ",notas)
   

# calculando el promedio
suma=0
for x in range(3):
    suma+=notas[x]
    
promedio=suma/3
print("el promedio es: ",promedio)

if promedio>1.7:
    print("aprobado")
else:
    print("aplazado")