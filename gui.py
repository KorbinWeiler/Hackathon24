from tkinter import *
from tkinter import ttk
import tkinter as tk
from math import floor
from core.program import *

#class to store indexes for each button
class clickHandler:

    def __init__(self, i,j, itemName ='', itemPrice = 0.0):
        self.i = i
        self.j = j
        self.itemName = itemName
        self.itemPrice = itemPrice

    #calls the onClick function with stored indexes
    def on_click(self):
        GUI.onClick(self.i, self.j, self.itemName, self.itemPrice)

class GUI:

    #Action on button press
    def onClick(height, width, name, price):
        
        #print(str((height * 10)-((10-5) * height)+width))
        if ((height * 10)-((10-5) * height)+width) == 34:
            box.delete(1.0, END)
        elif name == '':
            pass    
        else:
            box.insert(END, name + ": " + str(price) + "\n")
        return

    #Populates buttons on the screen
    def makeButtons(height, width):

        #list of buttons
        buttons = []

        #creates size * size buttons
        for i in range(width):
            for j in range(height):
                if ((i * 10)-((10-height) * i)+j) < len(currentMenu.items):
                    handler = clickHandler(i,j, currentMenu.items[(i * 10)-((10-height) * i)+j].name, currentMenu.items[(i * 10)-((10-height) * i)+j].price)
                    button = tk.Button(root, text=str(currentMenu.items[(i * 10)-((10-height) * i)+j].name) ,width=20, height = 4, padx=1, pady=1, command = handler.on_click)
                else:
                    handler = clickHandler(i,j)
                    button = tk.Button(root, text='' ,width=20, height = 4, padx=1, pady=1, command = handler.on_click)
                button.config(background="dark blue", fg = 'white')
                button.grid(column=j, row=i, sticky='nesw')
                #adds new button to the list
                buttons.append(button)
                if button['text'] == '34':
                    button.config(text='end order')
              
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
        currentSession = ProgramSession()
        currentSession.load_menu("tacobell")
        global currentMenu 
        currentMenu = currentSession.get_menu()
        GUI.buildWindow(915, 532, 'menu')
        GUI.purchasedItems()
        GUI.total()
        GUI.makeButtons(5, 7)
        root.mainloop()
        return
    
GUI.guiWrapper()