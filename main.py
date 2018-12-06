from graf import *
from tkinter import *

c = Canvas(width=800, height=400)
c.pack()
c.focus_set()

Mygraf = Graf(c,15)
velkost = Mygraf.zisti_priemer()

prvy = -1
def pohyb(event):
    global prvy
    clicked = False
    for i in range(Mygraf.zisti_pocet_vrcholov()):
        pos = Mygraf.zisti_pos_vrchola(i)
        if abs(pos[0] - event.x) < velkost and abs(pos[1] - event.y) < velkost:
            clicked = True
            if prvy == -1:
                prvy = i
            elif prvy != i:
                Mygraf.novy_sused(prvy, i)
                prvy = -1
    if not clicked:
        Mygraf.pridaj(event.x, event.y, e.get())
        prvy = -1

def farba():
    Mygraf.zafarbi()
    
Button(text='Farebny svet',command=farba).pack()

c.bind('<Button-1>', pohyb)

e=Entry()
e.pack(side='bottom')

mainloop()
