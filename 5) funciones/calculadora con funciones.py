# CALCULADORA CON FUNCIONES
print("calculadora con funciones:")

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def raiz(a,b=2):
    return a**1/b

def division(a,b):
    if b==0:
        return "no se puede dividir por CERO";
    else:
        return a/b
    

print("la suma de 3 y 4 son: ",suma(3,4));
print("la resta de 5 entre 4 es: ",resta(5,4));
print("la raiz de 144 es: ", raiz(144,2));
print("la multiplicacion de 2 por 3 es: ",multiplicacion(2,3));
print("la division es: ",division(6,3));