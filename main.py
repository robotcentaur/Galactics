#Galactics_Boss

import sys
from tkinter import *

decksize = 20
discard = 0 


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        #Buttons
        Draw = Button(frame, text='ATTACK PLAYER', command= bosscard)
        Draw.grid(row=0, column=1)
        Damage = Button(frame, text='DAMAGE BOSS', command= pressme)
        Damage.grid(row=2, column=1) 
        #Messages
        message1 = Message(frame, 
              text='BOSS')
        message1.grid(row=0, column=0)
        message2 = Message(frame, 
              text='GALACTIC LEAGUE MEMBERS')
        message2.grid(row=2, column=0)


def bosscard():
        global decksize
        global discard
        novi = Toplevel()
        canvas = Canvas(novi, width = 300, height = 300)
        canvas.pack(expand = YES, fill = BOTH)
        gif2 = PhotoImage(file = 'image2.gif')
        canvas.create_image(50, 10, image = gif2, anchor = NW)
        #assigned the gif2 to the canvas object
        canvas.gif2 = gif2
        discard =+ 1
        decksize = decksize - discard
        print (decksize)
        import random
        PLAYER_NUMBER = ['One', 'Two']
        AGGRO = ['Drain Die', 'Wipe Hand Card', 'Destroy Power', 'Damage', 'Minion']
        Dealer_Choice = random.choice(AGGRO)
        print(Dealer_Choice + ' ---> Player Number ' + random.choice(PLAYER_NUMBER))
        if Dealer_Choice is 'Minion':
            print('RELEASE THE HOUNDS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            minioncard()


def minioncard():
        novi = Toplevel()
        canvas = Canvas(novi, width = 300, height = 300)
        canvas.pack(expand = YES, fill = BOTH)
        gif3 = PhotoImage(file = 'image3.gif')
        canvas.create_image(50, 10, image = gif3, anchor = NW)
        #assigned the gif3 to the canvas object
        canvas.gif3 = gif3


def pressme():
        global decksize
        global discard
        novi = Toplevel()
        canvas = Canvas(novi, width = 300, height = 300)
        canvas.pack(expand = YES, fill = BOTH)
        gif1 = PhotoImage(file = 'image.gif')
        canvas.create_image(50, 10, image = gif1, anchor = NW)
        #assigned the gif1 to the canvas object
        canvas.gif1 = gif1
        discard =+ 1
        decksize = decksize - discard
        print (decksize)

root = Tk()
root.wm_title('Boss!')
app = App(root)
root.mainloop()
