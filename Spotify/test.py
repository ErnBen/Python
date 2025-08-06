from tkinter import Tk, Button
from reproductor import Reproductor
lista = ["Musica/Don't Fence Me In - Bing Crosby.mp3"]
musica = Reproductor(lista[0])

def reproducirMusica():
    musica.reproducir()

winamp = Tk()
winamp.title("Winamp")
winamp.geometry("200x100")

bPlay = Button (text="☢", command=reproducirMusica)
bPlay.place(x=50, y=50)

winamp.mainloop()