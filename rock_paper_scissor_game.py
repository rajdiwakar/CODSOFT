# Rock, Paper and Scissor Game

import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor : ")

computer_choice = random.choice(item_list)

print("User Choice = ",user_choice)
print("Computer choice = ",computer_choice)

if user_choice == computer_choice:
    print("Both Chooses Same : = Match Tie ")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper cover Rock = Computer Win")

    else:
        print("Rock smashes Scissor = You Win ")

elif user_choice == "Paper":
    if computer_choice== "Scissor":
        print("Scissor cuts Paper = Computer Win ")   

    else:
        print("Paper covers Rock = You Win ")

elif user_choice == "Scissor":
    if computer_choice == "Paper":
        print("Scissor cuts Paper = You win ")

    else:
        print("Rock smashes Scissor = Computer Win")                                     
                 
