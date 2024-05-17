print("calculadora de operaciones basicas con 2 valores");

a=int(input("ingrese el primer valor: "));
b=int(input("ingrese el segundo valor: "));

print("ingrse las opciones para relizar las operaciones: ");

print("1)suma \n 2)resta \n 3)producto \n 4)cociente")

opcion= int(input("ingrese la opcion: "));

if opcion==1:
    suma=a+b;
    print("la suma es: ",suma);
    
if opcion==2:
    resta=a-b;
    print("la resta es: ",resta);
    
if opcion==3:
    producto=a*b;
    print("la multiplicacion  es: ",producto);
    
if opcion==4 :
    cocioente= a/b;
    print("la divisin es: ", cocioente);
    
    
    