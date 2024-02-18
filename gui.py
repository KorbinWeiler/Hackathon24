from tkinter import *
from tkinter import ttk
import tkinter as tk
from math import floor

class GUI:

    #Action on button press
    def onClick(position):
        print("botton!")
        return

    #Populates buttons on the screen
    def makeButtons(height, width):

        #list of buttons
        buttons = []

        #creates size * size buttons
        for i in range(width):
            for j in range(height):
                button = tk.Button(root, text=str((i * 10)-((10-height) * i)+j), height = 2, width=floor(windowWidth / (width * 4)),
                                command=lambda i=i: GUI.onClick(i))
                button.grid(column=j,row=i, padx=1, pady=1)
                button.config(background="dark blue", fg = 'white')
            
                #adds new button to the list
                buttons.append(button)      
        return
    
    def purchasedItems(values="nothing"):
        box = tk.Text(root, width=20, padx=1, pady=1)
        box.grid(column=5, rowspan=9, sticky='ne')
        box.config(bg="dark blue", fg='white')
        box.insert(END, values)
        
    def total(values="nothing"):
        total = tk.Text(root, height=5, width=20, padx=1, pady=1)
        total.grid(column=5, rowspan=2, sticky='e')
        total.config(bg='dark blue', fg='white')
        total.insert(END, values)

    #Draws the window
    def buildWindow(width = 512, height = 512, name = "default"):
        global windowHeight
        global windowWidth
        windowHeight = height
        windowWidth = width

        #window setup
        global root
        root = Tk(className=name)
        root.config(bg='#08103d')
        root.geometry(str(windowWidth)+"x"+str(windowHeight))
        root.grid()
        return

    #calls all functions to run the gui
    def guiWrapper():
        GUI.buildWindow(1024,1024)
        GUI.purchasedItems()
        GUI.total()
        GUI.makeButtons(4, 11)
        root.mainloop()
        return
    
GUI.guiWrapper()