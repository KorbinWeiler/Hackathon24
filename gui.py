from tkinter import *
from tkinter import ttk

#window setup
root = Tk(className="Menu")
root.config(bg='#08103d')
root.geometry("512x512")
root.grid()

def onClick(position):
    print("botton!")
    return

def makeButtons(size):
    buttons = []
    for i in range(size):
        for j in range(size):
            button = ttk.Button(root, text=str((i * 10)-((10-size) * i)+j), width=10, command=lambda i=i: onClick(i)).grid(column=j,row=i)
            buttons.append(button)
    return

makeButtons(5)
root.mainloop()