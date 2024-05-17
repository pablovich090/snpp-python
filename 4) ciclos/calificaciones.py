

for i in range(3):
    user=input("ingrese su usuario: ");
    clave=int(input("ingrese su contraseña: "));
    if user=="admin" and clave==123:
        print("acceso otorgado...")
        break;
    elif i==3:
        print("acceso denegado")
    else:
        print("intente de nuevo")
