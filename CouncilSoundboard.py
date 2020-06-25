from playsound import playsound
import os
import sys
from tkinter import *

os.chdir(os.path.dirname(sys.argv[0]))

def smoochingTime():
    playsound('files/SmoochingTime.wav')

def announcement():
    playsound('files/Announcement.wav')

def heyPaisanos():
    playsound('files/HeyPaisanos.wav')

def yareYare():
    playsound('files/YareYare.wav')

def doTheMario():
    playsound('files/DoTheMario.wav')

def excuseMePrincess():
    playsound('files/ExcuseMePrincess.wav')

def mikuDead():
    playsound('files/MikuDead.wav')

def dominoMiku():
    playsound('files/CuteLikeMiku.wav')

def turnItDown():
    playsound('files/TurnDownTheMusic.wav')

def doubleFlusher():
    playsound('files/DoubleFlusher.wav')

def gamerCeiling():
    playsound('files/GamerCeiling.wav')

def helloThere():
    playsound('files/HelloThere.wav')

def megalovania():
    playsound('files/Megalovania.wav')

def sansTalking():
    playsound('files/SansTalking.wav')

def senate():
    playsound('files/Senate.wav')

def dinophobe():
    playsound('files/Dinophobe.wav')

top = Tk()
#add widgets here
smoochButton = Button(top, text = "Smooching Time", command  = smoochingTime)
smoochButton.pack(expand=YES)

announcementButton = Button(top, text = "I have an announcement to make", command = announcement)
announcementButton.pack(expand=YES)

paisanoButton = Button(top, text = "Hey paisanos!", command = heyPaisanos)
paisanoButton.pack(expand=YES)

yareButton = Button(top, text = "Yare yare daze", command = yareYare)
yareButton.pack(expand=YES)

marioButton = Button(top, text = "Do the mario", command = doTheMario)
marioButton.pack(expand=YES)

princessButton = Button(top, text = "Excuuuuse me, princess", command = excuseMePrincess)
princessButton.pack(expand=YES)

deadButton = Button(top, text = "Hatsune Miku is dead", command = mikuDead)
deadButton.pack(expand=YES)

dominoButton = Button(top, text = "Its cute, just like Miku", command = dominoMiku)
dominoButton.pack(expand=YES)

musicdownButton = Button(top, text = "Turn the music down", command = turnItDown)
musicdownButton.pack(expand=YES)

flusherButton = Button(top, text = "It was a double flusher", command = doubleFlusher)
flusherButton.pack(expand=YES)

gamerButton = Button(top, text = "Now the gamers will rise", command = gamerCeiling)
gamerButton.pack(expand=YES)

helloButton = Button(top, text = "Hello there", command = helloThere)
helloButton.pack(expand=YES)

megalovaniaButton = Button(top, text = "Megalovania", command = megalovania)
megalovaniaButton.pack(expand=YES)

sansButton = Button(top, text = "You're gonna have a bad time", command = sansTalking)
sansButton.pack(expand=YES)

senateButton = Button(top, text = "I am the senate", command = senate)
senateButton.pack(expand=YES)

dinophobeButton = Button(top, text = "Luigi, don't be a dinophobe", command = dinophobe)
dinophobeButton.pack(expand=YES)
   
top.mainloop()
