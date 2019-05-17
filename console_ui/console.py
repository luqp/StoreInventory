import os


class Console():
    STYLE_END = "\x1b[0m"
    COLOR_GRAY = "\x1b[1;30m"
    COLOR_GREEN = "\x1b[1;32m"
    COLOR_YELLOW = "\x1b[3;33m"
    COLOR_PURPLE = "\x1b[3;35m"
    WIDTH = 74
    
    @classmethod
    def clean_screen(cls):
        os.system("cls" if os.name == "nt" else "clear")
    
    @classmethod
    def notification(cls, subject, done, was="was" ):
        print()
        input(
            f"{cls.COLOR_YELLOW}"
            f"The {subject} {was} {done} ... [enter]"
            f"{cls.STYLE_END}")

    @classmethod
    def gray(cls, text):
        return f"{cls.COLOR_GRAY}{text}{cls.STYLE_END}"
        
    @classmethod
    def green(cls, text):
        return f"{cls.COLOR_GREEN}{text}{cls.STYLE_END}"

    @classmethod
    def yellow(cls, text):
        return f"{cls.COLOR_YELLOW}{text}{cls.STYLE_END}"

    @classmethod
    def print_border(cls, simbol="-"):
        amount_simbols = len(simbol)
        print(simbol * (cls.WIDTH // amount_simbols))

    @classmethod
    def print_banner(cls, title, simbol="-"):
        cls.clean_screen()
        spaces_number = (cls.WIDTH - len(title)) // 2
        cls.print_border(simbol)
        print(spaces_number * " ", title, spaces_number * " ")
        cls.print_border(simbol)
        print()

    @classmethod
    def show_values(cls, commands, values, simbol=" -"):
        for command, text in zip(commands, values):
            if "product price" in str(command):
                text = f"{text} cents"
            print(f"{command}{simbol} {text}")
        print()
        cls.print_border()

    @classmethod
    def print_field_added(cls, item):
        if not item:
            return
        fields = [cls.gray(field.replace("_", " ")) for field in item.keys()]
        values = [value for value in item.values()]
        cls.show_values(fields, values, ":")
    
    @classmethod
    def print_menu(cls, actions):
        texts = [action.__doc__ for action in actions.values()]
        commands = [cls.yellow(f"[{key}]") for key in actions.keys()]
        cls.show_values(commands, texts, "")

    @classmethod
    def print_item_details(cls, item):
        cls.print_banner(cls.green(item.product_name))
        print(f"Price: {item.product_price} cents")
        print(f"Quantity: {item.product_quantity}")
        print(f"Date update: {item.date_updated.strftime('%b/%d/%Y')}")
        print()
        cls.print_border()

    @classmethod
    def print_name_item(cls, data):
        names = [
            f"{item.product_name}" for item in data
        ]
        ids = [item.product_id for item in data]
        cls.show_values(ids, names, ")")
    
    @classmethod
    def options_whole_items(cls):
        print(
            cls.gray("write a"),
            cls.yellow("[number]"),
            cls.gray("or"),
            cls.yellow("[back]"),
            cls.gray("to return")
        )
    
    @classmethod
    def options_view(cls, number):
        print(
            "To see a item, insert a number between",
            cls.yellow("1"), "to",
            cls.yellow(number))
        print()
        print(
            cls.gray("Write"), cls.yellow("[show]"), 
            cls.gray("to show whole items"))
        print(
            cls.gray("Write"), cls.yellow("[back]"), 
            cls.gray("to return"))
        print()
        cls.print_border()
    
    @classmethod
    def options_item(cls):
        print(
            cls.yellow("[n]"),
            cls.gray("Next ·"),
            cls.yellow("[p]"),
            cls.gray("Previous ·"),
            cls.yellow("[q]"),
            cls.gray("Quit"))

    @classmethod
    def field_key_note(cls):
        print(cls.gray("Example price in $us: 14.0"))

    @classmethod
    def print_exit_message(cls):
        print()
        print(f"{cls.COLOR_PURPLE}...Closed app{cls.STYLE_END}")
        print()
