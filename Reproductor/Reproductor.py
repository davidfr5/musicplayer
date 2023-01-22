import pygame   
import tkinter as tk #used to develop GUI
from tkinter.filedialog import askdirectory 
import os #para interactuar con la interfaz

music_player = tk.Tk() 
music_player.title("QUE ESCUCHAMOS HOY JEFE?") 
music_player.geometry("450x250")
#Ask for a directory
directory = askdirectory()
os.chdir(directory) #it permits to chenge the current dir
song_list = os.listdir() #it returns the list of files song

play_list = tk.Listbox(music_player, font="Helvetica 12 bold", bg="grey", selectmode=tk.SINGLE)
for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

def play():
  

     pygame.mixer.music.load(play_list.get(tk.ACTIVE))
     var.set(play_list.get(tk.ACTIVE))
     pygame.mixer.music.play()
    
def stop():
    pygame.mixer.music.stop()
    
def pause():
    pygame.mixer.music.pause()
    
def unpause():
    pygame.mixer.music.unpause()

Button1 = tk.Button(music_player, width=4, height=3, font="Courier 12 bold", text="PLAY", command=play, bg="black", fg="white")
Button2 = tk.Button(music_player, width=4, height=3, font="Courier 12 bold", text="STOP", command=stop, bg="white", fg="black")
Button3 = tk.Button(music_player, width=4, height=3, font="Courier 12 bold", text="STOPPED", command=pause, bg="black", fg="white")
Button4 = tk.Button(music_player, width=4, height=3, font="Courier 12 bold", text="RUN", command=unpause, bg="white", fg="black")

var = tk.StringVar() 
song_title = tk.Label(music_player, font="Arial 12 bold", textvariable=var)
song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")

play_list.pack(fill="both", expand="yes")

music_player.mainloop()