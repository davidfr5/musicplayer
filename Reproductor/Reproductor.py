import pygame   
import tkinter as tkr #used to develop GUI
from tkinter.filedialog import askdirectory 
import os #para interactuar con la interfaz

music_player = tkr.Tk() 
music_player.title("QUE ESCUCHAMOS HOY JEFE?") 
music_player.geometry("450x250")

directory = askdirectory()
os.chdir(directory) #it permits to chenge the current dir
song_list = os.listdir() #it returns the list of files song

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg="grey", selectmode=tkr.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()
    
def pause():
    pygame.mixer.music.pause()
    
def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(music_player, width=4, height=3, font="Courier 12 bold", text="PLAY", command=play, bg="black", fg="white")
Button2 = tkr.Button(music_player, width=4, height=3, font="Courier 12 bold", text="STOP", command=stop, bg="white", fg="black")
Button3 = tkr.Button(music_player, width=4, height=3, font="Courier 12 bold", text="STOPPED", command=pause, bg="black", fg="white")
Button4 = tkr.Button(music_player, width=4, height=3, font="Courier 12 bold", text="RUN", command=unpause, bg="white", fg="black")

var = tkr.StringVar() 
song_title = tkr.Label(music_player, font="Arial 12 bold", textvariable=var)
song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")

play_list.pack(fill="both", expand="yes")

music_player.mainloop()