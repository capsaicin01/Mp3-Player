from tkinter import *
import pygame as py
import os

window = Tk()
window.title("Ton Player")
window.geometry("650x260")
window.config(bg="black")

py.init()
playstate = 0
mainb = PhotoImage(file="Icons/play.png")
pauseimage = PhotoImage(file="Icons/stop.png")
playimage = PhotoImage(file="Icons/play.png")


def playstop():
    global playstate
    if playstate == 0:
        song = songList.get(ACTIVE)
        py.mixer.music.load(f"Songs/{song}")
        py.mixer.music.play()
        playstate = 1
        mainButton.configure(image=pauseimage)
    elif playstate == 1:
        py.mixer.music.pause()
        playstate = 2
        mainButton.configure(image=playimage)
    else:
        py.mixer.music.unpause()
        playstate = 1
        mainButton.configure(image=pauseimage)


def nextSong():
    current = songList.curselection()
    next = songList.get(current[0] + 1)
    py.mixer.music.load(f"Songs/{next}")
    py.mixer.music.play(loops=0)
    songList.selection_clear(0, END)
    songList.activate(current[0] + 1)
    songList.selection_set(current[0] + 1)


def previousSong():
    current = songList.curselection()
    previous = songList.get(current[0]-1)
    py.mixer.music.load(f"Songs/{previous}")
    py.mixer.music.play(loops=0)
    songList.selection_clear(0, END)
    songList.activate(current[0] - 1)
    songList.selection_set(current[0] - 1)


# App Name
logo = PhotoImage(file="Icons/logo.png")
isim = Label(window, image=logo, text="Ton Player", bg="black", fg="#1db954", font="Helvetica 17", compound="left")
isim.pack()


# Song List
songList = Listbox(window, bg="black", fg="white", width=100, selectbackground="gray", highlightcolor="black", bd=1)
songList.pack()
for i in os.listdir("Songs"):
    if i.endswith(".mp3"):
        songList.insert(END, i)

tustakim = Frame(window)
tustakim.pack()

# Previous Button
previousb = PhotoImage(file="Icons/previous.png")
previousButton = Button(tustakim, bg="black", image=previousb, width=62, height=59, bd=0, command=previousSong)
previousButton.grid(row=0, column=0)

# Play Button
mainButton = Button(tustakim, bg="black", image=mainb, width=62, height=59, bd=0, command=playstop)
mainButton.grid(row=0, column=1)

# Next Button
skipb = PhotoImage(file="Icons/skip.png")
skipButton = Button(tustakim, bg="black", image=skipb, width=62, height=59, bd=0, command=nextSong)
skipButton.grid(row=0, column=2)

window.iconbitmap("Icons/logo.ico")
window.mainloop()
