## strings o cadenas de textos
print("STRINGS O CADENAS DE TEXTOS: ");

nombre= "pablo";
apellido= "galeano";

print(nombre +" "+ apellido);

texto= "este texto \n tiene salto de linea y \t tabulacion";
print(texto);

## formateo

print("formateos");

usuario, clave, email = "alex", 1234, "admin@admin.com";

print("su usuario y contraseña son: {} , {} y su email {} ".format(usuario, clave, email));
print("su usuario y contraseña son: %s, %d y su email %s" %(usuario, clave, email));
print("su usuario y contraseña son: " + usuario + "" + str(clave) + "y su email" + email);
print(f"su usuario y contraseña son: {usuario} {clave} y su email: {email} ");