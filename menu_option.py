from tracemalloc import start


class MenuOption:
    def __init__(self, index, option):
        self.index = index
        self.option = option

    def show_option(self):
        return(f"{self.index}. {self.option}")


