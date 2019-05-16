from collections import OrderedDict
from datetime import datetime

import re

from databases.inventory import Inventory, write_new_csv_file, update_item
from console_ui.console import Console


def view_item():
    while True:
        total_items = len(Inventory)
        text = f"You can insert a number between 1 to {total_items}\n"
        text += "Write back to return"
        Console.print_banner("V I E W  I T E M")
        Console.print_text(text)
        user_input = input("> ")
        if user_input == 'back':
            print("go out...")
            return True
        try:
            id_item = int(user_input)
        except ValueError:
            Console.input_error()
            continue
        else:
            if id_item in range(1, total_items + 1):
                item = Inventory.get_by_id(id_item)
                Console.print_item_details(item)
            else:
                input("Not exist this value, enter to try again")


def wait_valid_input(field):
    while True:
        value = input(f"Insert {field}: ")
        if field == "quiantity":
            try:
                value = int(value)
            except:
                continue
        elif field == "price":
            try:
                price = re.findall(r"\d+\.\d+", value)[0]
                value = round(float(price) * 100.00)
            except:
                continue
        if value:
            return value


def add_entry():
    fields = OrderedDict([
        ("name", "product_name"),
        ("price", "product_price"),
        ("quantity", "product_quantity")
    ])
    item = {}
    for field, key in fields.items():
        Console.print_banner("A D D  E N T R Y")
        Console.print_field_added(item)
        item[key] = wait_valid_input(field)
    try:
        inventory = Inventory.select().where(Inventory.product_name.contains(item['product_name']))
        if len(inventory):
            update_item(inventory, item, datetime.now())
        else:
            Inventory.create(**item)
    except:
        print("Not added")
        input()
    else:
        print("Added successfully")
        input()
    return True


def make_backup():
    write_new_csv_file()
    input("A backup was created")
    return True


def quit_menu():
    print("bye bye!!...")
    return False


def prompt_menu():
    actions = OrderedDict([
        ('v', ["View a single product's inventory", view_item]),
        ('a', ["Add a new product to database", add_entry]),
        ('b', ["Make a backup of the entire inventory", make_backup]),
        ('q', ["To quit", quit_menu])
    ])
    continue_ = True
    while continue_:
        Console.print_banner("M E N U", '/')
        Console.show_values(actions)
        answer = input("> ")

        if answer in actions:
            continue_ = actions[answer][-1]()
            continue
        input("Try again... enter to continue")            


if __name__ == "__main__":
    prompt_menu()
