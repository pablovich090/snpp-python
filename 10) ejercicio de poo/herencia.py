# area de triangulo y cuadrado:

class Reactangulo:
    base=None
    altura=None
    def __init__(self,b,a):
        self.base=b
        self.altura=a
    def area(self):
        return self.base*self.altura

class Cuadrado(Reactangulo):
    def __init__(self,lado):
        super().__init__(lado,lado)
        
        
if __name__=='__main__':
    rectangulo=Reactangulo(b=3,a=4)
    print("area del rectangulo: ",rectangulo.area())
    
    cuadrado=Cuadrado(lado=5)
    print("area del cuadrado: ",cuadrado.area())
    