import random

file = open("rating.txt", "w")
file.write("Tim 350\n")
file.write("Jane 200\n")
file.write("Alex 400\n")
file.close()

def get_lst():
    file = open("rating.txt", "r")
    info_lst = file.readlines()
    file.close()
    value_lst = []
    final_lst = []
    for i in info_lst:
        value_lst.append(i.replace("\n", " "))
    for i in value_lst:
        value = i.split()
        final_lst += value
    return final_lst

usr_name = input("Enter your name: ")
print("Hello, " + usr_name)
rating = 0
rating_list = get_lst()
for i in range(len(rating_list)):
    if rating_list[i] == usr_name:
        rating = int(rating_list[i + 1])
game_mode = input()

if game_mode == "rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire":
    print("Okay, let's start")

    winning = {
            'water': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
            'dragon': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
            'devil': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
            'lightning': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
            'gun': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
            'rock': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
            'fire': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
            'scissors': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
            'snake': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
            'human': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
            'tree': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
            'wolf': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
            'sponge': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
            'paper': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
            'air': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper']
        }

    while True:
        
        usr_option = input()
        option_list = ["rock", "gun", "lightning", "devil", "dragon", "water", "air", "paper", "sponge", "wolf", "tree", "human", "snake", "scissors", "fire"]
        other_option = ["!exit", "!rating"]
        option = random.choice(option_list)

        if (usr_option not in option_list) and (usr_option not in other_option):
            print("Invalid input")
        elif usr_option == "!rating":
            print("Your rating: " + str(rating))
        elif usr_option == "!exit":
            print("Bye!")
            break
        elif option == usr_option:
            print("There is a draw ({})".format(usr_option))
            rating += 50
        elif option in winning[usr_option]:
            print("Sorry, but the computer chose {}".format(option))
        elif option not in winning[usr_option]:            
            print("Well done. The computer chose {} and failed".format(option))
            rating += 100
        

elif game_mode == "":
    print("Okay, let's start")
    while True:
        
        usr_option = input()
        option_list = ["scissors", "paper", "rock"]
        option = random.choice(option_list)

        if (usr_option != "scissors" and usr_option != "paper") and (usr_option != "rock" and usr_option != "!exit") and usr_option != "!rating":
            print("Invalid input")
        elif usr_option == option:
            print("There is a draw ({})".format(usr_option))
            rating += 50
        elif usr_option == "paper" and option == "rock":
            print("Well done. The computer chose {} and failed".format(option))
            rating += 100
        elif usr_option == "scissors" and option == "paper":
            print("Well done. The computer chose {} and failed".format(option))
            rating += 100
        elif usr_option == "rock" and option == "scissors":
            print("Well done. The computer chose {} and failed".format(option))
            rating += 100
        elif option == "paper" and usr_option == "rock":
            print("Sorry, but the computer chose {}".format(option))
        elif option == "scissors" and usr_option == "paper":
            print("Sorry, but the computer chose {}".format(option))
        elif option == "rock" and usr_option == "scissors":
            print("Sorry, but the computer chose {}".format(option))
        elif usr_option == "!rating":
            print("Your rating: " + str(rating))
        elif usr_option == "!exit":
            print("Bye!")
            break
