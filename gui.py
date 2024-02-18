from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.filedialog as filedialog

from math import floor
from core.program import *

#class to store indexes for each button
class clickHandler:

    #clickerHandler initilizer
    def __init__(self, i,j, window, session, itemList = None, item = None):

        #declare class method
        self.window = window
        self.session = session 
        self.i = i
        self.j = j
        self.item = item
        self.itemList = itemList

    #calls the onClick function with stored indexes
    def on_click(self):
        GUI.onClick(self, self.i, self.j, self.itemList, self.item)

class GUI:

    def __init__(self):
        self.init_load_menu_path = None
        self.init_load_menu_path = filedialog.askopenfilename(initialdir=file_menus.get_menu_dir_path)

        #declare class members
        self.root = self.buildWindow(995, 532, 'menu')     
        self.orderItems = self.purchasedItems()
        self.orderTotal = self.total()
        self.session = self.makeSession()
        self.menu = self.makeMenu()

    #List current items
    def listItems(itemList):

        #reset listed items
        box.delete(1.0, END)

        #iterate through current order items list, and write names and prices to the text box
        for items in itemList:
            box.insert(END, items.name + ": " + str(items.price) + "\n")
        return

    #Action on button press
    def onClick(self, height, width, itemList, item):

        box.insert(END, item.name + ": " + str(item.price) + "\n")

        #Add new item into the session
        self.session.get_order_session().add(item)

        #Re-list current items and move text box to show most recent item
        GUI.listItems(itemList)
        box.see("end")

        #Update order total
        total.delete(1.0, END)
        total.insert(END, "Total: " + str("%.2f") % (self.session.get_order_session().get_order_total_charge()))

        return

    def end(self):
        #Clear item text box
        box.delete(1.0, END)

        #Reset session
        self.session.stop_order_session() 
        self.session.start_order_session()

    #Populates buttons on the screen
    def makeButtons(self, height, width):

        #list of buttons
        buttons = []

        #creates width * height buttons
        for i in range(width):
            for j in range(height):

                #checks if button index is within than the current number of items available
                if (i * height) + j < len(self.menu.items):

                    #Passes current i and j indexes along with new item and current order items
                    handler = clickHandler(i,j,self.root,self.session, self.session.get_order_session().get_order_items(), self.menu.items[(i * height) + j])

                    #Add new button displaying item name and price
                    button = tk.Button(self.root, text=str(self.menu.items[(i * height) + j].name) + '\n' + str(self.menu.items[(i * height) + j].price) 
                                       ,width=20, height = 4, padx=1, pady=1, command = handler.on_click)

                #Checks if it is the last button                       
                elif (i * height) + j == 34:


                    #Passes current i and j indexes
                    handler = clickHandler(i,j, self.root,self.session)

                    #Adds new button to end order
                    button = tk.Button(self.root, text='End Order' ,width=20, height = 4, padx=1, pady=1, command = self.end)

                #Not a valid item
                else:

                    #Passes current i and j indexes
                    handler = clickHandler(i,j, self.root,self.session)

                    #Adds a new blank button
                    button = tk.Button(self.root, text='' ,width=20, height = 4, padx=1, pady=1)

                #Connects all buttons and changes their color to dark blue with white text
                button.config(background="dark blue", fg = 'white')
                button.grid(column=j, row=i, sticky='nesw')

                #adds new button to the list
                buttons.append(button)
              
        return
    
    def purchasedItems(self,values = ''):
        global box
        box = tk.Text(self.root, width=30, padx=1, pady=1)
        box.grid(column=9,rowspan=5,sticky='nesw')
        box.config(bg="dark blue", fg='white')
        box.insert(END, values)
        
    def total(self, values=""):
        global total 
        total = tk.Text(self.root, width=30,height = 5, padx=1, pady=1)
        total.grid(column = 9, rowspan=2, sticky='nesw')
        total.config(bg='dark blue', fg='white')
        total.insert(END, values)

    #Draws the window
    def buildWindow(self, width = 512, height = 512, name = "default"):

        #window setup
        root = Tk(className=name)
        root.config(bg='#08103d')
        root.geometry(str(width)+"x"+str(height))
        root.grid()
        root.resizable(width=False, height=False)
        return root
    
    def makeSession(self):
        session= ProgramSession()
        if self.init_load_menu_path:
            session.load_menu_from_path(self.init_load_menu_path)
        else:
            session.load_menu("tacobell")
        session.start_order_session()
        return session

    def makeMenu(self):
        menu = self.session.get_menu()
        return menu

    #calls all functions to run the gui
    def guiWrapper(self):
        
        self.makeButtons(5, 7)
        self.root.mainloop()
        return