# file_deser module
# handles reading and writing menus to files

import csv
import core.file_config
import core.menu as menu

FFORMAT_QUOTE_CHAR = '"'
FFORMAT_DELIMITER = ','

def get_menu_path(menu_name):
    return core.file_config.MENU_FILES_DIR + '/' + menu_name + '.menu'

# todo: add an option to use exact path and open up prompts to choose paths
def load_menu(menu_name: str):
    menu_data = core.menu.Menu(name="") # will extract the name data later
    menu_path = get_menu_path(menu_name)
    with open(menu_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=FFORMAT_DELIMITER, quotechar=FFORMAT_QUOTE_CHAR, skipinitialspace=True)
        name_row = next(reader)
        assert name_row is not None and name_row[0] is not None, "in menu file, missing menu name row"
        # print("menu name:", name_row[0])
        menu_data.name = name_row[0]
        for item_row in reader:
            # get common item fields
            item_kind = item_row[0]
            assert item_kind is not None, "in menu-file item row, missing item kind field."
            item_name = item_row[1]
            assert item_name is not None, "in menu-file item row, missing item name field."
            item_price = item_row[2]
            assert item_price is not None, "in menu-file item row, missing item price field."

            if item_kind == "I":    # item kind, corresponds to single item
                menu_data.def_item(item_name, item_price)
            elif item_kind == "M":  # meal kind, corresponds to collection of items
                # TODO: this ...
                pass
            else:
                raise RuntimeError("invalid item kind in menu-file item row.")
    return menu_data

def save_menu(menu_data):
    menu_path = get_menu_path(menu_data.name)
    with open(menu_path, "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=FFORMAT_DELIMITER, quotechar=FFORMAT_QUOTE_CHAR)
        # write menu name header row
        writer.writerow([menu_data.name])
        # write menu item rows
        for item in menu_data.items:
            if item.kind == "Item":
                writer.writerow(["I", item.name, item.price])
            if item.kind == "Meal":
                #TODO
                pass