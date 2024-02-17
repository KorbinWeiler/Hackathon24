class Item:
    name = ""
    price = 0
    # todo: add metatadata like item pngs, etc, ...

class Meal:
    name = ""
    price = 0
    items = []
    # todo: other metadata

class Menu:
    items = [] # array of Items or Meals

class OrderItem:
    item: None # reference to the item data
    amt: 0 # number for that item

class OrderSession:
    order_items = []

class ProgramSession:
    order = None
    loadedMenus = None
