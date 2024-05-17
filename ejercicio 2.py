'''
Escribí un programa que solicite al usuario ingresar la cantidad de
kilómetros recorridos por una motocicleta y la cantidad de litros de
combustible que consumió durante ese recorrido. Mostrar el
consumo de combustible por kilómetro
'''

print("KILOMETROS RECORRIDOS Y COMBUSTIBLE CONSUMIDO");

km=int(input("ingrese los kilometros recorrido: "));

'''
la motocicleta consume 5 litos cada 3 kilometros
'''

litros_consumidos= (km/3)*5;
print("la cantidad de combustible quemado es: ", litros_consumidos, "litros");