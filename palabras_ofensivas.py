'''Crea una aplicación que busque palabras ofensivas dentro de una web.
En caso de encontrarlos, deberá enviar una notificación.'''

from urllib import request
from urllib.error import URLError

palabras_malas=['puto','imbecil','coño','marica','culiao','idiota','pelotudo']

def ver_contenido(url):
    try:
        f= request.urlopen(url)
    except URLError:
        return('la url' + url + 'no existe')
    else:
        aux=f.read()
        contenido=aux.split()
        palabras_encontradas=[]
        cantidad_po=0
        for i in palabras_malas:
            for con in contenido:
                if i in con.decode():
                    palabras_encontradas.append(i)
                
        return palabras_encontradas    
                
    


url='https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales'
print("-------------------------------------------------------------")
print("informe del sitio")
print(ver_contenido(url))
