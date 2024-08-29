import customtkinter
import tkinter
import os
from pygame import mixer
from tkinter import filedialog

pencere = customtkinter.CTk()
pencere.geometry("400x500")
pencere.resizable(False,False)
pencere.title("Music Player")

mixer.init()
def gözat():

    global filename
    filename = filedialog.askopenfilename(filetypes=[("Müzik Dosyaları","*.mp3*")])
    if filename:
        sarkıad.configure(text=os.path.basename(filename))
        mixer.music.load(filename)

def play():
    mixer.music.play()

def stop():
    mixer.music.stop()

def sesayarla(vol):
    ses = float(sesayar.get()/100)
    mixer.music.set_volume(ses)





sarkıad=customtkinter.CTkLabel(pencere,text="Geçerli Şarkı Yok")
sarkıad.pack()
gözat = customtkinter.CTkButton(pencere,text="Gözat",command=gözat)
gözat.pack()
baslat = customtkinter.CTkButton(pencere,text="Oynat",command=play)
baslat.pack()
durdur = customtkinter.CTkButton(pencere,text="Durdur",command=stop)
durdur.pack()
sesayar = customtkinter.CTkSlider(pencere,from_=0,to=100,command=sesayarla)
sesayar.pack()

pencere.mainloop()
