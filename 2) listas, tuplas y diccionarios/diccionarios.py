# diccionarios

productos={"manzana": 5600, "banana": 4500, "sandia": 8600};

print("precio de las frutas: ")
print(productos);

pais_capital={
    "paraguay":"asuncion",
    "argentina":"buenos aieres",
    "bolivia": "la paz",

}
print(pais_capital);
print(pais_capital["bolivia"])

# cargado un diccionario:
print("cargando diccionario")
dic={}





def cargar(usuario,contraseña):
    dic[usuario]=contraseña
    
if __name__=="__main__":
    cargar("admin","123")
    cargar("pali","321")
    
