import core.file_menus as file_menus

# params item: the item object to create order item from
def item_order_new(item):
    return []

# params: item_order - order, menu - menu object to get item object from
def item_order_item(item_order, menu):
    pass

class OrderSession:
    def __init__(self, menu):
        self.ordered = []
        self.menu = menu
        self.cached_charge = 0

    # params: item - menu item object
    def add(self, item, qt=1):
        io = item_order_new(item)
        self.ordered.append(item)

    def remove(self, item, qt=1):
        # TODO:
        pass

    def get_order_items(self):
        return []

    def get_order_item_counts(self):
        return []
    
    def get_order_total_charge(self):
        return self.cached_charge

class ProgramSession:
    # todo: add data to integrate with gui stuff
    def __init__(self):
        self.menu = None
        self.order_session = None

    def start_order_session(self):
        if self.order_session is not None:
            return False
        self.order_session = OrderSession()
        return True

    def stop_order_session(self):
        self.order_session = None
        return True
    
    # loads the menu into the memory and is referenced by the program sessions
    def load_menu(self, menu_name):
        self.menu = file_menus.load_menu(menu_name)

    # returns None if no current order session, returns item order list if current order session
    def get_order_session(self):
        return self.order_session

    # returns None if no menu is loaded, otherwise returns the menu
    def get_menu(self):
        return self.menu