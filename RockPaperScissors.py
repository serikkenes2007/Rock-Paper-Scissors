from math import tan, tanh
from tkinter import *
from tkinter import font
import random

t = Tk()


def rock2_click():
    i = Label(f, text="ROCK", bg="green")
    i.place(relx=0, rely=0.2, relwidth=0.1, relheight=0.1)
    lst = [1, 2, 3]
    ll = random.choice(lst)
    if ll == 1:
        ok = Label(f, text="ROCK", bg="pink")
        ok.place(relx=0, rely=0.6, relheight=0.1, relwidth=0.1)
    elif ll == 2:
        kok = Label(f, text="PAPER", bg="pink")
        kok.place(relx=0, rely=0.6, relheight=0.1, relwidth=0.1)
    else:
        zx = Label(f, text="SCISSORS", bg="pink")
        zx.place(relx=0, rely=0.6, relheight=0.1, relwidth=0.1)
    if ll == 1 and rock2_click:
        bkop = Label(f, text="DRAW", bg="yellow")
        bkop.place(relx=0.8, rely=0, relwidth=0.1, relheight=0.1)
    elif ll == 2 and rock2_click:
        nji = Label(f, text="LOSE", bg="yellow")
        nji.place(relx=0.8, rely=0, relwidth=0.1, relheight=0.1)
    elif ll == 3 and rock2_click:
        mko = Label(f, text="WIN", bg="yellow")
        mko.place(relx=0.8, rely=0, relwidth=0.1, relheight=0.1)


def paper2_click():
    uysa = Label(f, text="PAPER", bg="green")
    uysa.place(relx=0, rely=0.2, relwidth=0.1, relheight=0.1)
    lst = [1, 2, 3]
    xm = random.choice(lst)
    if xm == 1:
        xh = Label(f, text="ROCK", bg="pink")
        xh.place(relx=0, rely=0.6, relheight=0.1, relwidth=0.1)
    elif xm == 2:
        xd = Label(f, text="PAPER", bg="pink")
        xd.place(relx=0, rely=0.6, relheight=0.1, relwidth=0.1)
    else:
        qx = Label(f, text="SCISSORS", bg="pink")
        qx.place(relx=0, rely=0.6, relheight=0.1, relwidth=0.1)
    if xm == 1 and paper2_click:
        rasd = Label(f, text="WIN", bg="yellow")
        rasd.place(relx=0.8, rely=0, relwidth=0.1, relheight=0.1)
    elif xm == 2 and paper2_click:
        dsar = Label(f, text="DRAW", bg="yellow")
        dsar.place(relx=0.8, rely=0, relwidth=0.1, relheight=0.1)
    elif xm == 3 and paper2_click:
        wasd = Label(f, text="LOSE", bg="yellow")
        wasd.place(relx=0.8, rely=0, relwidth=0.1, relheight=0.1)


def scissors2_click():
    tylo = Label(f, text="SCISSORS", bg="green")
    tylo.place(relx=0, rely=0.2, relwidth=0.1, relheight=0.1)
    lst = [1, 2, 3]
    zr = random.choice(lst)
    if zr == 1:
        zy = Label(f, text="POCK", bg="pink")
        zy.place(relx=0, rely=0.6, relheight=0.1, relwidth=0.1)
    elif zr == 2:
        zpo = Label(f, text="PAPER", bg="pink")
        zpo.place(relx=0, rely=0.6, relheight=0.1, relwidth=0.1)
    else:
        zsr = Label(f, text="SCISSORS", bg="pink")
        zsr.place(relx=0, rely=0.6, relheight=0.1, relwidth=0.1)
    if zr == 1 and scissors2_click:
        hjk = Label(f, text="LOSE", bg="yellow")
        hjk.place(relx=0.8, rely=0, relwidth=0.1, relheight=0.1)
    elif zr == 2 and scissors2_click:
        vbn = Label(f, text="WIN", bg="yellow")
        vbn.place(relx=0.8, rely=0, relwidth=0.1, relheight=0.1)
    elif zr == 3 and scissors2_click:
        ghy = Label(f, text="DRAW", bg="yellow")
        ghy.place(relx=0.8, rely=0, relwidth=0.1, relheight=0.1)


def start_click():
    cv = Button(f, text="Rock", command=rock2_click)
    cv.place(relx=0.1, rely=0.8, relheight=0.1, relwidth=0.25)
    klj = Button(f, text="Paper", command=paper2_click)
    klj.place(relx=0.4, rely=0.8, relheight=0.1, relwidth=0.25)
    asd = Button(f, text="Scissors", command=scissors2_click)
    asd.place(relx=0.7, rely=0.8, relheight=0.1, relwidth=0.25)


t.geometry('600x450')
can = Canvas(height=450, width=600)
can.pack()
f = Frame(can, bg="red")
f.place(relheight=1, relwidth=1)
loli = Label(f, text="ROCK,PAPER,SCISSORS", bg="white", font=50)
loli.pack()
hu = Button(f, text="START", bg="white", command=start_click)
hu.place(relx=0.25, rely=0.2, relheight=0.2, relwidth=0.5)

t.mainloop()
