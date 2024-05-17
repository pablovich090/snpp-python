class Persona:
    nombre=None
    edad=None
    
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def mostrar(self):
        return f"{self.nombre}, edad: {self.edad}"
    
class Empleado(Persona):
    sueldo_bruto=None
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self.sueldo_bruto=sueldo
        
    def mostrar(self):
        return super().mostrar() + f", SN: {self.calcular_salario_neto()}"
    def calcular_salario_neto(self):
        return self.sueldo_bruto * 0.9
    
class Cliente(Persona):
    contacto_telefono=None
    def __init__(self,tel):
        self.contacto_telefono=tel
    def mostrar(self):
        return super().mostrar() + f", tel:{self.contacto_telefono}"
    
    
if __name__=="__main__":
    x=Cliente("pablo",19,1200,123321)
    
    print(Cliente.mostrar())