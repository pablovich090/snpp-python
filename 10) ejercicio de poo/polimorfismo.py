# persona que camina y persona que anda en bici, ambos se desplazan

class Persona:
    nombre=None
    def __init__(self,nom):
        self.nombre=nom
    def avanza(self):
        return ("yo me desplazo caminando")

class Ciclista(Persona):
    def __init__(self, nom):
        super().__init__(nom)
    def avanza(self):
        return ("yo me muevo en bicileta")
    
if __name__=='__main__':
    persona=Persona("pablo")
    print("soy pablo y ", persona.avanza())
    
    ciclista=Ciclista("Carlos")
    print("soy carlos y ",ciclista.avanza())