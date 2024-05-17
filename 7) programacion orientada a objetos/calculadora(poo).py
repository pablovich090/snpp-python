class Calculadora:
    numero_1=None
    numero_2=None
    resultado=None
    historial=None
    

    def __init__(self,n,m):  #constructor
        self.numero_1=m
        self.numero_2=n
        self.resultado=0 
        self.historial=[]
    
    def sumar(self):
        return self.numero_1 + self.numero_2

    def restar(self):
        return self.numero_1 - self.numero_2

    def multiplicar(self):
        return self.numero_1 * self.numero_2

    def dividir(self):
        return self.numero_1 / self.numero_2
    def set_numeros(self,x,y):
        self.numero_1=x
        self.numero_2=y

if __name__=="__main__":
    casio=Calculadora(8,2) # materializacion o instancia
    print("suma: ",casio.sumar())
    print("resta: ",casio.restar())
    print("producto: ",casio.multiplicar())
    print("cociente: ",casio.dividir())
    
    
    
    
    