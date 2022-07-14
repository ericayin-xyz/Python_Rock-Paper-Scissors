from email import message
from email.policy import default
from menu_option import MenuOption
from menu import Menu
from menu_seed import menu, menu_options
import random
from art import *
from bullet import Password
from os import system
from unicodedata import name
from images import logo, mainmenu, rock, paper, scissors,rock_paper_scissors, line, win_a, win_b, lose_a, lose_b, options_menu
from player import Player
from menu_seed import tips, menu_scores_option


def _print_options(i):
    opt = input(f"\n  Select your option (1-{i}):  ")
    return opt

def _inviad_input():
    message1 = tprint("error", font = "small")
    message2 = print("- Inviad Input -\n")
    message_output = message1 and message2
    return message_output

def _exit_game():
    tprint("See  you\nNext  Game . . ", font = "small")

def _totall_score(i):
    score_cap = i
    return score_cap

# ----------------------------------------------------#
system('clear') 
images = [rock, paper, scissors]
option = ""
options = ""
score_choices = ""
totall_score = 3






# main menu has 4 options, select one of them
while option != "4":
    # display logo + weclome str
    menu.print_menu()
    # variables
    user_score = 0
    computer_score = 0
    
    option = _print_options(4)
    system('clear')

    # select option 1 - player1
    if option == "1":
        name1 = input("\nEnter your name:\n")
        new_player = Player(1, name1)
        system('clear')
        new_player.welcome_player()
        # make the game repeatable
        while user_score < totall_score and computer_score < totall_score:
            try:
                # ask user for a choice
                print(f"{'-'*11}\n1. Rock\n2. Paper\n3. Scissors\n{'-'*11}\n[4. End the game]\n\n\n")           
                user_choice = int(new_player.ask_choice())
            except ValueError:
                system('clear')
                print(rock_paper_scissors)
                print("\nIvalid Input, please enter a number.\n")  
            else:    
                #clear the screen between rounds.
                system('clear')
                if user_choice > 4 or user_choice < 1:
                    _inviad_input()
                elif user_choice == 4:
                    break
                else:
                    print("\n\/\/")
                    print(name1)
                    print(images[user_choice - 1])
                    print(line)

                    # generate a random choice for the computer
                    computer_choice = random.randint(1,3)
                    print("\/\/\nComputer")
                    print(images[computer_choice - 1])

                    # give feedback + core keeping
                    if user_choice == 3 and computer_choice == 1:
                        computer_score += 1
                        print(f">> You Lose! <<\nYour score: {user_score}\nComputer score: {computer_score}\n\n")
                    elif user_choice == 1 and computer_choice == 3:
                        user_score += 1
                        print(f">> You Win! <<\nYour score: {user_score}\nComputer score: {computer_score}\n\n")
                    elif user_choice == computer_choice:
                        print(f">> It's a Deaw! <<\nYour  score: {user_score}\nComputer score: {computer_score}\n\n")
                    elif user_choice > computer_choice:
                        user_score += 1
                        print(f">> You Win! <<\nYour  score: {user_score}\nComputer score: {computer_score}\n\n")
                    elif user_choice < computer_choice:
                        computer_score += 1
                        print(f">> You Lose! <<\nYour score: {user_score}\nComputer score: {computer_score}\n\n")
        # check who is the winer  
        # if user goes to 3 then the game should stop and print "win"
        if user_score == totall_score:
            print(win_a)
            print(win_b)

        # if computer goes to 3 then the game should stop and print "lose"
        elif computer_score == totall_score:
            print(lose_a)
            print(lose_b)
        else:
            _exit_game()

    # select option 2 - player2
    elif option == "2":
        user1_score = 0
        user2_score = 0
        name1 = input("\nEnter Player 1 name:\n")
        name2 = input("\nEnter Player 2 name:\n")

        newplayer1 = Player(1, name1)
        newplayer2 = Player(2, name2)

        system('clear')
        print(f"\nWelcome {name1} and {name2}!\n")

        while user1_score < totall_score and user2_score < totall_score:
            try:
                # print 4 options
                print(f"{'-'*11}\n1. Rock\n2. Paper\n3. Scissors\n{'-'*11}\n[4. End the game]\n\n\n")

                # ask user 1 and user 2 for a choice
                user_input_1 = Password(prompt=f"Make your choice, {name1}!\n", hidden="*")
                user_choice_1 = int(user_input_1.launch())
                user_input_2 = Password(prompt=f"Make your choice, {name2}!\n", hidden="*")
                user_choice_2 = int(user_input_2.launch())
                
            except ValueError:
                system('clear')
                print(rock_paper_scissors)
                print("\nIvalid Input, please enter a number.\n")  
            else:    
                #clear the screen between rounds.
                system('clear')
                if user_choice_1 > 4 or user_choice_1 < 1 or user_choice_2 > 4 or user_choice_2 < 1:
                    _inviad_input()
                elif user_choice_1 == 4 or user_choice_2 == 4:
                    break
                else:
                    # print results -> user 1
                    print("\n\/\/")
                    print(name1)
                    print(images[user_choice_1 - 1])
                    print(line)
                    # print results -> user 2
                    print("\n\/\/")
                    print(name2)
                    print(images[user_choice_2 - 1])

                    # check who is the winer   
                    # give feedback + core keeping
                    if user_choice_1 == 3 and user_choice_2 == 1:
                        user2_score += 1
                        print(f">> {name2} Wins! <<\n{name1} score: {user1_score}\n{name2} score: {user2_score}\n\n")
                    elif user_choice_1 == 1 and user_choice_2 == 3:
                        user1_score += 1
                        print(f">> {name1} Wins! <<\n{name1} score: {user1_score}\n{name2} score: {user2_score}\n\n")
                    elif user_choice_1 == user_choice_2:
                        print(f">> It's a Deaw! <<\n{name1}  score: {user1_score}\n{name2} score: {user2_score}\n\n")
                    elif user_choice_1 > user_choice_2:
                        user1_score += 1
                        print(f">> {name1} Wins! <<\n{name1}  score: {user1_score}\n{name2} score: {user2_score}\n\n")
                    elif user_choice_1 < user_choice_2:
                        user2_score += 1
                        print(f">> {name2} Wins! <<\n{name1} score: {user1_score}\n{name2} score: {user2_score}\n\n")

        # if user goes to 3 then the game should stop and print "win"
        if user1_score == totall_score:
            print(win_a)
            tprint(f"\n> > >  {name1}\n", font = "small")

        # if computer goes to 3 then the game should stop and print "lose"
        elif user2_score == totall_score:
            print(win_a)
            tprint(f"\n> > >  {name2}\n", font = "small")
        else:
            _exit_game()

    elif option == "3":
        while True:
            try:
                menu_options.print_menu()
                options = _print_options(3)
                system('clear')
            except ValueError:
                _inviad_input()

            if options == "1":
                while True:
                    try:
                        menu_scores_option.print_menu()
                        score_choices = _print_options(3) 
                    except ValueError:
                        _inviad_input()
                    else:    
                        if score_choices < "4" and score_choices > "0":
                        # if score_choices == "1" or "2" or "3":
                            score_list = {"1" : 3, "2" : 5, "3" : 10}
                            totall_score = score_list[score_choices]             
                            if score_choices == "1": 
                                print(f"\n  Your score has been changed to [{totall_score}] !")
                            elif score_choices == "2":
                                print(f"\n  Your score has been changed to [{totall_score}] !")
                            elif score_choices == "3":
                                print(f"\n  Your score has been changed to [{totall_score}] !")
                            else:
                                break 
                        else:
                            system('clear')  
                            _inviad_input()
                        break 

            # type 2 - direction/rules about the game    
            elif options == "2":
                print(tips)

            # type 3 - back to main menu
            elif options == "3":
                tprint("Ready ?", font = "small")
                break
            
            else:
                _inviad_input()
            input("\n\n>> Press ENTER to back << ")      
            system('clear') 
            continue
    
    # select option 4 - exit
    elif option == "4":
        continue

    else:
        _inviad_input()

    input("\n>> Press ENTER to continue <<")
    system('clear')

# end the game
tprint("Goodbye!", font = "small")
