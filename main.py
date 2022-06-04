import random

while True:
    list_of_choice = ["Rock", "Paper", "Scissors"]
    Player = input("Pick an option, R for Rock, P for Paper or S for Scissors: ").upper()
    if Player not in ['R', 'P', 'S']:
        print("Invalid input")
        continue
    CPU = random.choice(list_of_choice)
    user_option = ["R", "P", "S"]
    user_index = user_option.index(Player)
    user_option[0] = list_of_choice[0]
    user_option[1] = list_of_choice[1]
    user_option[2] = list_of_choice[2]
    user = user_option[user_index]
    if user == "Rock" and CPU == "Scissors":
        print(f'player {user} : CPU {CPU}')
        print("You Win")
        break
    elif user == "Rock" and CPU == "Paper":
        print(f'player {user} : CPU {CPU}')
        print("computer win")
        break
    elif user == "Paper" and CPU == "Scissors":
        print(f'player {user} : CPU {CPU}')
        print("computer win")
        break
    elif user == "Paper" and CPU == "Rock":
        print(f'player {user} : CPU {CPU}')
        print("You win")
        break
    elif user == "Scissors" and CPU == "Rock":
        print(f'player {user} : CPU {CPU}')
        print("computer win")
        break
    elif user == "Scissors" and CPU == "Paper":
        print(f'player {user} : CPU {CPU}')
        print("You Win")
        break
    else:
        print(f'player {user} : CPU {CPU}')
        print("Tie replay: ")
