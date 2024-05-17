from biblioteca import Biblioteca
from libro import Libro

if __name__=='__main__':
    ejecutar=True
    
    while ejecutar:
        print("BIENVENIDO AL SISTEMA BIBLIOTECARIO")
        op=int(input("¿que vas a hacer?\n 1-crear biblioteca\n 2-agregar libro\n 3-ver catalogo\n 4-quitar libros\n 5-salir\n"))
        if  op==1:
            nombre=input("nombre de la biblioteca: ")
            biblioteca=Biblioteca(nombre)
            print("se creo la biblioteca: ",biblioteca.consultar_nombre_biblioteca())
        elif op==2:
            titulo=input("titulo: ")
            autor=input("autor: ")
            cant_pag=int(input("Paginas: "))
            genero=input("genero: ")
            sinopsis=input("sinopsis: ")
            libro=Libro(titulo,autor,cant_pag,genero,sinopsis)
            biblioteca.agregar_libro(libro)
        elif op==3:
            print("catalogo de libros: ")
            for i in biblioteca.consultar_libros():
                print(i)
        elif op==4:
            indice=int(input("id del libro a eliminar: "))
            biblioteca.quitar_libro(indice)
        elif op==5:
            print("gracias por la visita")
            ejecutar=False
        else:
            print("opcion incorrecta")