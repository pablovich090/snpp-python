from pygame import mixer
class Reproductor:
    #atributos
    archivo=None
 #constructor
    def __init__(self,archivo):
        self.archivo=archivo
        mixer.init()
        mixer.music.load(archivo)
        
    def play(self):
        mixer.music.play()
        return "reproducioendo musica"
    
    def stop(self):
        mixer.music.stop()
        return "la musica paro"
    
    def volume(self,v):
        mixer.music.set_volume(v)
        return "definiendo volumen a {}".format(v)