from tkinter import *
from tkinter import messagebox
import random

def no ():
    messagebox.showinfo ('', 'Eu tambem ')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk ()
root.geometry ('680x608')
root.title ('survey')
root.resizable (width=False, height=False )
root['bg'] = 'white'

Label = Label(root, text= 'Quer fazer dar certo?' , font='Arial 40 bold' , bg='white' ) .pack ()
btnYes = Button(root, text='Sim' , font='Arial 20 bold')
btnYes.place(x=170, y=190)
btnYes.bind( '<Enter>', motionMouse)
btnNo = Button(root, text=' Com toda certeza', font='Arial 20 bold', command=no) .place(x=350, y=100)

root.mainloop ()