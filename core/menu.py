class Item:
    kind = "Item"
    def __init__(self, name="", price=0):
        self.name = name
        self.price = price

    def print_item(self):
        print(f"item:{self.name}, price:{self.price}")

class Meal:
    kind = "Meal"
    def __init__(self, name="", price=0, items=None):
        self.name = name
        self.price = price
        if items is not None:
            self.items = items
        else:
            self.items = []

    def def_items(self, items):
        self.items = items

    def print_item(self):
        print(f"item:{self.name}, price:{self.price}, items:{self.items}")
    

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

    def def_meal(self, name, price):
        new_meal = Meal(name=name, price=price)
        self.items.append(new_meal)
        return new_meal

    def item_from_name(self, name):
        for item in self.items:
            if name == item.name:
                return item
        return None
    

    def print_items(self):
        for item in self.items:
            item.print_item()
