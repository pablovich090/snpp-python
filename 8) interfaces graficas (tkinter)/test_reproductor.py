from tkinter import*
from tkinter.ttk import*
from reproductor import*

musica=Reproductor('wefere.mp3')

def play_musica():
    musica.volume(0.20)
    musica.play()
    
master= Tk()
master.geometry("200x200")

label=Label(master,text="Reproductor de musica")
label.pack(pady=10)

#boton de reproducir
btn_play=Button(master,text="reproducir", command=play_musica)
btn_play.pack(pady=10)

# boton de parar
btn_stop=Button(master,text="parar", command=musica.stop)
btn_stop.pack(pady=10)

# boton de volumen
btn_volume=Button(master,text="volumen ++", command=musica.volume)
btn_volume.pack(pady=10)



mainloop()