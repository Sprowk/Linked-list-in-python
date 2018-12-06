from graf import *
from tkinter import *

c = Canvas(width=800, height=400)
c.pack()
c.focus_set()

Igor = Graf(c,15)
velkost = Igor.zisti_priemer()

prvy = -1
def pohyb(event):
    global prvy
    clicked = False
    for i in range(Igor.zisti_pocet_vrcholov()):
        pos = Igor.zisti_pos_vrchola(i)
        if abs(pos[0] - event.x) < velkost and abs(pos[1] - event.y) < velkost:
            clicked = True
            if prvy == -1:
                prvy = i
            elif prvy != i:
                Igor.novy_sused(prvy, i)
                prvy = -1
    if not clicked:
        Igor.pridaj(event.x, event.y, e.get())
        prvy = -1

c.bind('<Button-1>', pohyb)

e=Entry()
e.pack(side='bottom')

mainloop()
