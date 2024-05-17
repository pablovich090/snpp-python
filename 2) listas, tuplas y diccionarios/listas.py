
## LISTAS:

alumnos=["dario","juan","ramiro","ana","sofia"];

print("esto es una lista: ");
print(alumnos);

print( "mostrando un rango de elementos: ",alumnos[0:2]); ''' DE ESTA MANERA SE IMPRIME UN RANGO O SLICES, ES PARA MOSTRAS CIERTOS 
ELEMENTOS DE LA LISTA
'''

# lista con distintos datos
mn=["piña",True,890,"noni"];
print("lista con distintos datos: ", mn);

# lista dentro de otra lista
lista_con_lista=("hola mundo",False,123,["mario","luis","rafa"]);
print("lista dentro de otra lista:");
print("lista variada: ", lista_con_lista[3][2]);

# agregar elemtos a la lista:
alumnos.append("elias");
print("lista actualizada...");
print(alumnos);

## removiedo elementos de una lista..
print("removiendo elementos:");
print("lista sin remover elementos: ",mn);
mn.remove("noni");
print("lista con elememto removido: ",mn);

