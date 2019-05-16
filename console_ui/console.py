import os


class Console():

    @classmethod
    def clean_screen(cls):
        os.system("cls" if os.name == "nt" else "clear")

    @classmethod
    def show_values(cls, commands, values, simbol=" -"):
        for command, text in zip(commands, values):

            if command == "product price":
                text = f"{text} cents"
            print(f"{command}{simbol} {text}")
        print()
        print("-" * 74)

    @classmethod
    def print_field_added(cls, item):
        if not item:
            return
        fields = [field.replace("_", " ") for field in item.keys()]
        values = [value for value in item.values()]
        cls.show_values(fields, values, ":")
    
    @classmethod
    def print_menu(cls, actions):
        texts = [action.__doc__ for action in actions.values()]
        commands = [f"[{key}]" for key in actions.keys()]
        cls.show_values(commands, texts, "")

    @classmethod
    def print_banner(cls, title, simbol="-"):
        cls.clean_screen()
        size_total = 74
        amount_simbols = len(simbol)
        spaces_number = (size_total - len(title)) // 2
        
        print(simbol * (size_total // amount_simbols))
        print(spaces_number * " ", title, spaces_number * " ")
        print(simbol * (size_total // amount_simbols))
        print()
    
    @classmethod
    def print_text(cls, text):
        print(text)
    
    @classmethod
    def notification(cls, subject, done, was="was" ):
        print()
        input(f"The {subject} {was} {done} ... [enter]")

    @classmethod
    def print_item_details(cls, item):
        cls.print_banner(f"{item.product_name}", " ")
        print(f"Price: {item.product_price}")
        print(f"Quantity: {item.product_quantity}")
        print(f"Date update: {item.date_updated.strftime('%b/%d/%Y')}")
        print()
        print("-" * 74)


    @classmethod
    def print_exit_message(cls):
        print("...App closed")

    @classmethod
    def priint_name_item(cls, data):
        names = [
            f"{item.product_name} - {item.product_quantity}" for item in data
        ]
        ids = [item.product_id for item in data]
        cls.show_values(ids, names, ")")
    
    @classmethod
    def options_view(cls, number):
        cls.print_text(f"To see a item, insert a number between 1 to {number}")
        cls.print_text("Write [back] to return")
        cls.print_text("Write [show] to show whole items")
        print()
        print("-" * 74)
