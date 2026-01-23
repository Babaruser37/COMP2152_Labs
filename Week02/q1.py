import random
choices = ["Rock", "Paper", "Scissors"]

player_choice = input("Please enter a number between 1 - 3")

try:
    player_choice = int(player_choice) 
    player_tool = choices[player_choice - 1]

except:
    print(f"{player_choice} is not a valid input, please try again")

computer_choice = random.randint(0,2)
computer_tool = choices[computer_choice]

if computer_tool == player_tool:
    print(f"You selected {player_tool} and the computer selected {computer_tool}. It's a TIE!")
elif player_tool == choices[0] and computer_tool == choices[2]:
    print(f"You selected {player_tool} and the computer selected {computer_tool}. You WIN!")
elif player_tool == choices[1] and computer_tool == choices[0]:
    print(f"You selected {player_tool} and the computer selected {computer_tool}. You WIN!")
elif player_tool == choices[2] and computer_tool == choices[1]:
    print(f"You selected {player_tool} and the computer selected {computer_tool}. You WIN!")
else:
    print(f"You selected {player_tool} and the computer selected {computer_tool}. You LOSE :(")

if player_tool != "Rock":
    print("You did not pick classic Rock")