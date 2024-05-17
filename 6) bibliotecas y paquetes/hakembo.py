import random

while True:
    aleatorio=random.randrange(0,3)
    elijePc=""
    print("1.piedra")
    print("2.papel")
    print("3.tijera")
    opcion=int(input("elige tu opcion: "))
    if opcion==1:
        elige_usuario="piedra"
    elif opcion==2:
        elige_usuario="papel"
    elif opcion==3:
        elige_usuario="tijera"
    print("ejegiste: ", elige_usuario)
    
    if aleatorio==0:
        elijePc="piedra"
    elif aleatorio==1:
        elijePc="papel"
    elif aleatorio==2:
        elijePc="tijera"
    print("la maquina eligio:",elijePc)
    
    print("...........")
    
    if elijePc=="piedra" and elige_usuario=="papel":
        print("ganaste, papal envuelve piedra")
    elif elijePc=="papel "and elige_usuario=="tijera":
        print("ganaste, tijera conta papel")
    elif elijePc=="tijera" and elige_usuario=="piedra":
        print("ganaste, piedra machaca tijera")
    elif elijePc=="papel" and elige_usuario=="piedra":
        print("perdiste, papel envuelve a la piedra")
    elif elijePc=="tijera" and elige_usuario=="papel":
        print("perdiste, tejer corta papel")
    elif elijePc=="piedra" and elige_usuario=="tijera":
        print("perdiste, piedra machaca tijera")
    elif elige_usuario==elijePc:
        print("empate:")
