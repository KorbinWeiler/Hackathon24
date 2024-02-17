from tkinter import *
from tkinter import ttk
import tkinter as tk
from math import floor

#window setup
root = Tk(className="Menu")
root.config(bg='#08103d')
root.geometry("512x512")
root.grid()

def onClick(position):
    print("botton!")
    return

def makeButtons(height, width):

    #list of buttons
    buttons = []
    buttonSize = root.winfo_geometry
    print(buttonSize)

    #creates size * size buttons
    for i in range(width):
        for j in range(height):
            button = tk.Button(root, text=str((i * 10)-((10-height) * i)+j), height = 2, width=floor(root.winfo_width() * width),
                                command=lambda i=i: onClick(i))
            button.grid(column=j,row=i, padx=1, pady=1)
            button.config(background="dark blue", fg = 'white')
            
            #adds new button to the list
            buttons.append(button)      
    return

makeButtons(5, 10)
root.mainloop()