import re

# note: these should have analagous functions in the gui code ...
def cmd_load_menu(): {}

def cmd_save_menu(): {}

def cmd_create_menu() : {}

def cmd_edit_menu() : {}

def cmd_def_item(): {}

def cmd_undef_item(): {}

command_action = {
    # todo: implement function handlers in these
    # format: [action_context, ...]

    # menu actions
    'load-menu': ['menu', cmd_load_menu],
    'save-menu': ['menu', cmd_save_menu],
    'create-menu': ['menu', cmd_create_menu],
    'edit-menu': ['menu', cmd_edit_menu],

    #create actions
    'def-item': ['create'],
    'undef-item': ['create'],
    'save-edits': ['create'],

    # order actions
    'add' : ['order'],
    'remov': ['order'],
}

flag_re_pattern = re.compile("-\w=\w*")

def print_menu_usage():
    print("menu usage:")
    print("1. load [menu path]")
    print("2. save [menu path] [menu name]")
          
def print_order_usage():
    print("order usage:")
    print("1. add [item/meal name] -q=[quantity]")
    print("2. remove [item/meal name] -q=[quantity]")

def get_command_action():
    line = input(">>")
    print("entered: " + line)
    return line

def proc_command_action(line: str):
    args = []
    toks = line.split()
    
    args.append[toks[0]]
    toks.remove(0)

    for tok in toks:
        # if tok is flag argument
        flag_match = re.fullmatch(

        )
        # if tok is single argument ...
        

def run():
    print("Hello world from command app.")
    while True:
        line = get_command_action()
        proc_command_action(line)

