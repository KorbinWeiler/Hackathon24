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
    name = ""
    items = [] # array of Items or Meals

    def __init__(self, *, name):
        self.name = name

    def def_item(self, name, price):
        new_item = Item()
        new_item.name = name
        new_item.price = price

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