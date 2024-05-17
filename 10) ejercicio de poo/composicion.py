# RELACION DE COMPOSICION

class Automovil:
    
    def __init__(self,modelo,marca,color):
        self.modelo=modelo
        self.marca=marca
        self.color=color
        self.estado='en reposo'
        self.motor=Motor(cilindros=4)
    
    def acelerar(self,tipo='despacio'):
        if tipo=='rapida':
            self.motor.inyecta_gasolina(10)
        else:
            self.motor.inyecta_gasolina(3)
            
    def get_info_auto(self):#retorna informacion del motor
        return(self.modelo, self.marca, self.color) 
    
class Motor:
    def __init__(self,cilindros,tipo='diesel'):
        self.cilindros=cilindros
        self.tipo=tipo
        self.temperatura=0
    def inyecta_gasolina(self,cantidad):
        pass
    def get_info_motor(self):#retorna info del motor
        return(self.cilindros, self.tipo)
    
if __name__=='__main__':
    mi_motor=Motor(4,'nafta')
    mi_auto=Automovil('patrol','nissan','blanco')
    mi_auto.motor=mi_motor
    mi_auto.acelerar('rapida')
    
    print("datos del vehiculo: ", mi_auto.get_info_auto())
    print("datos del motor: ",mi_motor.get_info_motor())
        


    
    

        