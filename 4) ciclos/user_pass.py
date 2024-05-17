# Datos de usuario y contraseña correctos
usuario_correcto = "usuario123"
contraseña_correcta = "contraseña123"

# Contador de intentos
intentos = 3

while intentos > 0:
    # Solicitar usuario y contraseña al usuario
    usuario = input("Ingrese el usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    # Verificar usuario y contraseña
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Acceso concedido.")
        break
    else:
        intentos -= 1
        print(f"Acceso denegado. Te quedan {intentos} intentos.")

# Si se agotan los intentos
if intentos == 0:
    print("Has agotado todos tus intentos. El programa se cerrará.")


# UTLILIZANDO EL CICLO FOR:

# Datos de usuario y contraseña correctos
usuario_correcto = "usuario123"
contraseña_correcta = "contraseña123"

# Número máximo de intentos
max_intentos = 3

for intento in range(max_intentos, 0, -1):
    # Solicitar usuario y contraseña al usuario
    usuario = input("Ingrese el usuario: ")
    contraseña = input("Ingrese la contraseña: ")

    # Verificar usuario y contraseña
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Acceso concedido.")
        break
    else:
        print(f"Acceso denegado. Te quedan {intento - 1} intentos.")

# Si se agotan los intentos
else:
    print("Has agotado todos tus intentos. El programa se cerrará.")