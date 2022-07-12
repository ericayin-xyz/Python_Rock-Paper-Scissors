class MenuOption:
    def __init__(self, index, option):
        self.index = index
        self.option = option

    def show_option(self):
        print(f"  [{self.index}] {self.option}")

