from tkinter import *
from tkinter import ttk
import tkinter as tk
from math import floor
from core.program import *

#class to store indexes for each button
class clickHandler:

    def __init__(self, i,j, item = None):
        self.i = i
        self.j = j
        self.item = item

    #calls the onClick function with stored indexes
    def on_click(self):
        GUI.onClick(self.i, self.j, self.item)

class GUI:

    #Action on button press
    def onClick(height, width, item):
        if (height * 5) + width == 34:
            box.delete(1.0, END)
            currentSession.stop_order_session()
            currentSession.start_order_session()
        elif item.name == '':
            pass    
        else:
            box.insert(END, item.name + ": " + str(item.price) + "\n")
            currentSession.get_order_session().add(item)
            total.delete(1.0, END)
            total.insert(END, "Total: " + str("%.2f") % (currentSession.get_order_session().get_order_total_charge()))
            box.see("end")
        return

    #Populates buttons on the screen
    def makeButtons(height, width):

        #list of buttons
        buttons = []

        #creates size * size buttons
        for i in range(width):
            for j in range(height):
                if (i * height) + j < len(currentMenu.items):
                    handler = clickHandler(i,j, currentMenu.items[(i * height) + j])
                    button = tk.Button(root, text=str(currentMenu.items[(i * height) + j].name) + '\n' + str(currentMenu.items[(i * height) + j].price) ,width=20, height = 4, padx=1, pady=1, command = handler.on_click)
                elif (i * height) + j == 34:
                    handler = clickHandler(i,j)
                    button = tk.Button(root, text='end order' ,width=20, height = 4, padx=1, pady=1, command = handler.on_click)
                else:
                    handler = clickHandler(i,j)
                    button = tk.Button(root, text='' ,width=20, height = 4, padx=1, pady=1, command = handler.on_click)
                button.config(background="dark blue", fg = 'white')
                button.grid(column=j, row=i, sticky='nesw')

                #adds new button to the list
                buttons.append(button)
              
        return
    
    def purchasedItems(values = ''):
        global box
        box = tk.Text(root, width=30, padx=1, pady=1)
        box.grid(column=9,rowspan=5,sticky='nesw')
        box.config(bg="dark blue", fg='white')
        box.insert(END, values)
        
    def total(values=""):
        global total 
        total = tk.Text(root, width=30,height = 5, padx=1, pady=1)
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
        global currentSession 
        currentSession= ProgramSession()
        currentSession.load_menu("tacobell")
        currentSession.start_order_session()
        global currentMenu 
        currentMenu = currentSession.get_menu()
        GUI.buildWindow(995, 532, 'menu')
        GUI.purchasedItems()
        GUI.total()
        GUI.makeButtons(5, 7)
        root.resizable(width=False, height=False)
        root.mainloop()
        return