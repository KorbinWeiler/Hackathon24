import core.file_menus as file_menus

class OrderSession:
    def __init__(self, menu):
        self.ordered = []
        self.menu = menu
        self.tracked_charge = 0

    # params: item - menu item object
    def add(self, item, qt=1):
        self.tracked_charge += item.price
        self._add_rec(item)

    # params: item - menu item object
    # note: will enter inf recursion if a meal item is cyclicaly pointing to itself
    def _add_rec(self, item):
        if item.kind == "Item":
            self.ordered.append(item)
        elif item.kind == "Meal":
            for item_in_meal in item.items:
                self._add_rec(item_in_meal)
                

    def remove(self, item, qt=1):
        # TODO:
        
        pass

    def get_order_items(self):
        return self.ordered

    def get_order_item_counts(self):
        return []
    
    def get_order_total_charge(self):
        return self.tracked_charge

class ProgramSession:
    # todo: add data to integrate with gui stuff
    def __init__(self):
        self.menu = None
        self.order_session = None

    def start_order_session(self):
        if self.order_session is not None:
            return False
        self.order_session = OrderSession(self.menu)
        return True

    def stop_order_session(self):
        self.order_session = None
        return True
    
    # loads the menu into the memory and is referenced by the program sessions
    def load_menu(self, menu_name):
        self.menu = file_menus.load_menu(menu_name)

    # loads menu into memory, directly from path
    def load_menu_from_path(self, menu_path):
        self.menu = file_menus.load_menu_from_path(menu_path)

    # returns None if no current order session, returns item order list if current order session
    def get_order_session(self):
        return self.order_session

    # returns None if no menu is loaded, otherwise returns the menu
    def get_menu(self):
        return self.menu