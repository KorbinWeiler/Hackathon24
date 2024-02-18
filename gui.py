from tkinter import *
from tkinter import ttk
import tkinter as tk
from math import floor

#class to store indexes for each button
class clickHandler:

    def __init__(self, i,j):
        self.i = i
        self.j = j

    #calls the onClick function with stored indexes
    def on_click(self):
        GUI.onClick(self.i, self.j)

class GUI:

    #Action on button press
    def onClick(height, width):
        
        print("column " + str(height + 1) + "; row " + str(width + 1))
        box.insert(END, str(height + 1) + " " + str(width + 1) + "\n")
        return

    #Populates buttons on the screen
    def makeButtons(height, width):

        #list of buttons
        buttons = []

        #creates size * size buttons
        for i in range(width):
            for j in range(height):
                handler = clickHandler(i,j)
                button = tk.Button(root, text='button',width=20, height = 4, command = handler.on_click)
                button.config(background="dark blue", fg = 'white')
                button.grid(column=j, row=i, sticky='nesw')
                #adds new button to the list
                buttons.append(button)
                   
        return
    
    def purchasedItems(values = ''):
        global box
        box = tk.Text(root, width=20, padx=1, pady=1)
        box.grid(column=9,rowspan=5,sticky='nesw')
        box.config(bg="dark blue", fg='white')
        box.insert(END, values)
        
    def total(values=""):
        total = tk.Text(root, width=20,height = 5, padx=1, pady=1)
        total.grid(column = 9, rowspan=2, sticky='nesw')
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
        GUI.buildWindow(915, 532)
        GUI.purchasedItems()
        GUI.total()
        GUI.makeButtons(5, 7)
        root.mainloop()
        return
    
GUI.guiWrapper()