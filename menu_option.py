class MenuOption:
    def __init__(self, index, option):
        self.index = index
        self.option = option

    def show_option(self):
        print(f"  [{self.index}] {self.option}")



# class TotalScore:
#     def __init__(self, index):
#         self.index = index

#     def _show_score(self):
#         score_cap = self.index
#         return score_cap

# score = TotalScore(3)
# print(score._show_score)



# def _totall_score(i):
#     score_cap = i
#     return score_cap

# default_score = _totall_score("3")

# new_score = default_score.replace(_totall_score("5"))

# print(new_score)
 