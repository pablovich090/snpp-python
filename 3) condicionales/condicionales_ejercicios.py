a=int(input("ingrese el primer numero: "));
b=int(input("ingrese el sugundo numero: "));

if a>b:
    print(f"{a} es mayor a {b}")
    if a %2 ==0 :
        print("el numero ",a ,"es par");
    else:
        print(f"{a} es impar");
elif a<b :
    print(f"{b} es el mayor");
    if b%2==0:
        print(b," es par");
    else:
        print(f"{b} es impar");
else: 
    print("los numeros son iguales");

print("..................................................................");

user=input("ingrese su usuario: ");
clave=int(input("ingrese su contraseña: "));

if user=="admin" and clave==1234:
    print("acceso otorgado")
else:
    print("acceso denegado");