from tkinter import *
from tkinter import ttk
import tkinter as tk
from math import floor
from core.program import *

#class to store indexes for each button
class clickHandler:

    #clickerHandler initilizer
    def __init__(self, i,j, itemList = None, item = None):
        self.i = i
        self.j = j
        self.item = item
        self.itemList = itemList

    #calls the onClick function with stored indexes
    def on_click(self):
        GUI.onClick(self.i, self.j, self.itemList, self.item)

class GUI:

    #List current items
    def listItems(itemList):

        #reset listed items
        box.delete(1.0, END)

        #iterate through current order items list, and write names and prices to the text box
        for items in itemList:
            box.insert(END, items.name + ": " + str(items.price) + "\n")
        return

    #Action on button press
    def onClick(height, width, itemList, item):

        #check if the "End Order" button is pressed
        if (height * 5) + width == 34:

            #Clear item text box
            box.delete(1.0, END)

            #Reset session
            currentSession.stop_order_session() 
            currentSession.start_order_session()

        #Invalid input
        elif item == None:
            pass 

        #Valid item is entered   
        else:

            #Add new item into the session
            currentSession.get_order_session().add(item)

            #Re-list current items and move text box to show most recent item
            GUI.listItems(itemList)
            box.see("end")

            #Update order total
            total.delete(1.0, END)
            total.insert(END, "Total: " + str("%.2f") % (currentSession.get_order_session().get_order_total_charge()))

        return

    #Populates buttons on the screen
    def makeButtons(height, width):

        #list of buttons
        buttons = []

        #creates width * height buttons
        for i in range(width):
            for j in range(height):

                #checks if button index is within than the current number of items available
                if (i * height) + j < len(currentMenu.items):

                    #Enter 
                    handler = clickHandler(i,j,currentSession.get_order_session().get_order_items(), currentMenu.items[(i * height) + j])
                    button = tk.Button(root, text=str(currentMenu.items[(i * height) + j].name) + '\n' + str(currentMenu.items[(i * height) + j].price) ,width=20, height = 4, padx=1, pady=1, command = handler.on_click)
                elif (i * height) + j == 34:
                    handler = clickHandler(i,j,currentSession.get_order_session().get_order_items())
                    button = tk.Button(root, text='End Order' ,width=20, height = 4, padx=1, pady=1, command = handler.on_click)
                else:
                    handler = clickHandler(i,j,currentSession.get_order_session().get_order_items())
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