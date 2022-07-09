import random

scissors = '''
                  ._____
            _____/    ___)_____.
                          ______) 
                         _______)
            ____    (_____)
                ` __(____)

'''

rock = '''
                ._____
            ___/    ___)_.
                   (______) 
                   (______)
            __     (_____)
               ` __(____)
   
        '''

paper = '''
                ._____.
            ___/    ___)_____.
                        ______) 
                        _______)
            __         _______)
               \ .________)
   
        '''

images = [rock, paper, scissors]

print("Welcome come to the Rock Paper Scissors!\n")
user_choice = int(input("1. Rock\n2. Paper\n3. Scissors\n\nWhat do you choose?\n"))

print('''                                             -----
                                            | YOU |
                                             -----''')
print(images[user_choice - 1])
print('''
|-------------------------------------------------|
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
|—————————————————————————————————————————————————|
''')
computer_choice = random.randint(0,2)
print(images[computer_choice])

if user_choice > 3 or user_choice - 1 < 0:
    print("Ivalid Input: You Lose!")
elif user_choice - 1 == computer_choice:
    print("It's a Deaw")
elif user_choice - 1 > computer_choice:
    print("You Win!")
elif user_choice - 1 == 3 and computer_choice == 1:
    print("You Lose!")
elif user_choice - 1 == 1 and computer_choice == 3:
    print("You Win!")