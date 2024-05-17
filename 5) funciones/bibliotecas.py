import os
 
# menu principal
respuesta= -1;

while respuesta !=0:
    print("elija una opcion")
    print("1.Calculadora")
    print("2.ver mi pc")
    print("3.administrador de tarea")
    print("4.apagar equipo en 5 minutos")
    print("5.cancelar apagado")
    print("0. salir")
    respuesta=int(input("ingrese una respuesta: "))
    if respuesta==1:
        os.system('calc')
    elif respuesta==2:
        os.system('ipconfig')
    elif respuesta==3:
        os.system('taskmge')
    elif respuesta==4:
        os.system('shutdown -s -t 300')
    elif (respuesta==5):
        os.system('')
        #ver como cancelar el apagado
    else:
        "no se selecciono nada"