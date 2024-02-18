class OrderSession:
    def __init__(self):
        self.ordered = []

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
    def load_menu(path: str):
        pass

    # returns None if no current order session, returns item order list if current order session
    def get_order_session(self):
        return self.order_session

    # returns None if no menu is loaded, otherwise returns the menu
    def get_menu(self):
        return self.menu