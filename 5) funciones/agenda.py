
agenda={};
def cargar_agenda(nombre,telefono):
    agenda[nombre]=telefono

def ver_agenda():
    print(agenda)

def ver_agenda_detalle():
    print("lista de contactos");
    for nombre,tel in agenda.items():
        print(f"{nombre}:{tel}")


if __name__=="__main__":
    cargar_agenda("pepe","0987789963")
    cargar_agenda("lalo","0992238862")
    ver_agenda()
    ver_agenda_detalle();


