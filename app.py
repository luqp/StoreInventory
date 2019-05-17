from collections import OrderedDict

import re

from databases.inventory import Inventory
from console_ui.console import Console
from register import Register


register = Register(
        Inventory, 
        ['product_name', 'product_price', 'product_quantity', 'date_updated']
    )

def go_through_items(id_item, len_total):
    while True:
        Console.options_item()
        answer = input("> ").lower()
        if answer == 'q':
            return
        elif answer == 'n':
            id_item += 1
        elif answer == 'p':
            id_item -= 1
        if id_item > len_total:
            id_item = 0
        elif id_item < 1:
            id_item = len_total
        show_item_details(id_item, len_total)


def show_item_details(id_item, len_items):
    if id_item in range(1, len_items + 1):
        item = register.data.get_by_id(id_item)
        Console.print_item_details(item)
        return True
    else:
        Console.notification("input", "isn't exist", "")
        return False


def validate_to_show_item(user_input, len_items):
    try:
        id_item = int(user_input)
    except ValueError:
        Console.notification("input", "isn't valid", "")
        return
    else:
        if show_item_details(id_item, len_items):
            go_through_items(id_item, len_items)


def show_whole_items():
    while True:
        registers = register.data.select()[:]
        Console.print_banner(
            Console.green("Product Name")
        )
        Console.print_name_item(registers)
        Console.options_whole_items()
        user_input = input("> ").lower()
        if user_input == "back":
            return False
        validate_to_show_item(user_input, len(registers))


def view_item():
    """ View a single product's inventory"""
    is_looking = True
    while is_looking:
        items = len(register.data)
        Console.print_banner("V I E W   I T E M S", "~")
        Console.options_view(items)
        user_input = input("> ").lower()
        if user_input == 'back':
            is_looking = False
            continue
        if user_input == "show":
            is_looking = show_whole_items()
            continue
        validate_to_show_item(user_input, items)


def wait_valid_input(field):
    while True:
        parameter = field.replace("product_", "")
        value = input(f"Insert {parameter}: ")
        if field == "product_quantity":
            try:
                value = int(value)
            except:
                continue
        elif field == "product_price":
            try:
                price = re.findall(r"\d+\.?\d+?", value)[0]
                value = round(float(price) * 100.00)
            except:
                continue
        if value:
            return value


def add_entry():
    """ Add a new product to database """
    item = {}
    for field_key in register.fileds:
        Console.print_banner("A D D   E N T R Y", "~")
        Console.print_field_added(item)
        if field_key == "date_updated":
            continue
        if field_key == "product_price":
            Console.field_key_note()
        item[field_key] = wait_valid_input(field_key)
    try:
        register.fill_records([item])
    except ValueError:
        Console.notification("product", "not added")
    else:
        Console.notification("product", "added successfully")


def make_backup():
    """ Make a backup of the entire inventory """
    if register.make_a_backup():
        Console.notification("backup", "created")
    else:
        Console.notification("backup", "not created")


def quit_menu():
    """ Quit app """
    Console.print_exit_message()
    return True


def prompt_menu():
    actions = OrderedDict([
        ('v', view_item),
        ('a', add_entry),
        ('b', make_backup),
        ('q', quit_menu)
    ])
    quit_ = False
    while not quit_:
        Console.print_banner("M E N U", '<>')
        Console.print_menu(actions)
        answer = input("> ").lower()
        if answer in actions:
            quit_ = actions[answer]()
            continue
        Console.notification("input", "not correct")       


if __name__ == "__main__":
    try:
        if not len(register.data):
            raise ValueError
    except:
        register.create_database()
    prompt_menu()
