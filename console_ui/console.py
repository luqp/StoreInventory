import os


class Console():

    @classmethod
    def clean_screen(cls):
        os.system("cls" if os.name == "nt" else "clear")

    @classmethod
    def show_values(cls, options, simbol=" ->"):
        for command, text in options.items():
            if isinstance(text, list):
                text = text[0]
            print(f"{command}{simbol} {text}")

    @classmethod
    def print_banner(cls, title, simbol="-"):
        cls.clean_screen()
        size_total = 75
        spaces_number = (size_total - len(title)) // 2

        print(simbol * size_total)
        print(spaces_number * " ", title, spaces_number * " ")
        print(simbol * size_total)
        print()
    
    @classmethod
    def print_text(cls, text):
        print(text)
        print()

    @classmethod
    def print_item_details(cls, item):
        cls.print_banner(f"{item.product_name}", "*")
        cls.print_text("Details:")
        print(f"Price: {item.product_price}")
        print(f"Quantity: {item.product_quantity}")
        print(f"Date update: {item.date_updated.strftime('%b/%d/%Y')}")
        input("To continue, press enter...")
    
    @classmethod
    def print_field_added(cls, item):
        cls.show_values(item, ":")


    @classmethod
    def input_error(cls):
        input("Your input is not correct, try again, press enter to continue")