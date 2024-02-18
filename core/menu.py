class Item:
    kind = "Item"
    def __init__(self, name="", price=0):
        self.name = name
        self.price = price

class Meal:
    kind = "Meal"
    def __init__(self, name="", price=0):
        self.name = name,
        self.price = price
        self.items = []

class Menu:
    name = ""

    def __init__(self, *, name):
        self.name = name
        self.items = []

    def def_item(self, name, price):
        # TODO: check for repeat item names
        new_item = Item(name=name, price=price)
        self.items.append(new_item)
        return new_item

    def undef_item_byref(self, item):
        # TODO: handle errors here
        self.items.remove(item)
        
    def undef_item_byname(self, item_name): {}
        # just do a linear seach for item by name, maybe throw an error if item cannot be 

    def print_items(self):
        print("listing items of menu " + self.name)
        for item in self.items:
            print(f'name: {item.name}, price: {item.price}')