# CARGAR E IMPRIMIR UNA LISTA:

# PASO 1 : DEFINIMOS UNA LISTA VACIA
lista=[];

# PASO 2: DEFINIMOS LA FINCION PARA CARgAR LA LISTA
def carga_lista(dato):
    lista.append(dato)

# PASO 3: recibir una cantidad indetermindo de argumentos
def cargar_lista(*args):
    for arg in args:
        lista.append(arg)

def imprimir_lista():
    for item in lista:
        print(item, end='|')

 
# EJECUTAMOS LAS FUNCIONES
cargar_lista(25);
cargar_lista(50);
cargar_lista(75);
cargar_lista(100);

# imprimimos la lista
imprimir_lista() 
cargar_lista('A','B','C',[125,852,963])
imprimir_lista()