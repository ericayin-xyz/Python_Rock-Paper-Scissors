import random
from images import rock, paper, scissors

images = [rock, paper, scissors]

print("Welcome come to the Rock Paper Scissors!\n")
user_choice = int(input("1. Rock\n2. Paper\n3. Scissors\n\nWhat do you choose?\n"))
if user_choice > 3 or user_choice < 1:
    print("Ivalid Input: You Lose!")
else:
    print('''                                             -----
                                                | YOU |
                                                -----''')
    print(images[user_choice - 1])
    print('''
|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
    ''')
    computer_choice = random.randint(1,3)
    print(images[computer_choice - 1])


    if user_choice == 3 and computer_choice == 1:
        print("You Lose!")
    elif user_choice == 1 and computer_choice == 3:
        print("You Win!")
    elif user_choice == computer_choice:
        print("It's a Deaw")
    elif user_choice > computer_choice:
        print("You Win!")
    elif user_choice < computer_choice:
        print("You Lose!")


# else:
#     print("Ivalid Input: You Lose!")

    # |—————————————————————————————————————————————————|

# |-------------------------------------------------|
