#Functions
from ast import While
import random
def pick_a_door():
    doors = ['1', '2', '3']
    false_door = random.choice(doors)
    return false_door

def anomalies():
    anomolies_list = [
        "darkness",
        "an endless stairwell",
        "a mirror hallway",
        "a room full of clocks ticking ramblingly",
        "an abandoned space station",
        "your childhood home",
        "a ghost town"
    ]
    anomoly = random.choice(anomolies_list)
    return anomoly

#Game body
Doors_opened = 0
print("Welcome to the Pick a Door game! Start the game? (yes/no)")
input_response = input().strip().lower()
while input_response == 'yes':
    print("There are 3 doors infront of you: Door 1, Door 2, and Door 3. Pick one to go through: (1/2/3)")
    false_door = pick_a_door()
    player_choice = int(input())
    if str(player_choice) == false_door:
        print(f"Oh no! You picked Door {false_door} and you got lost in {anomalies()}! Game Over.")
        print("Would you like to try again? (yes/no)")
        input_response = input().strip().lower()
        if input_response == 'yes':
            Doors_opened = 0
        else:
            print("Thanks for playing! See you next time!")
            break
    else:
        print(f"Congratulations! Everything seems normal behind Door {player_choice}. Let's move on.")
        Doors_opened += 1
    if Doors_opened == 5:
        print("Amazing! You've navigated through 5 doors whitout encountering any anomalies! You won!")
        print("Do you want to play again? (yes/no)")
        input_response = input().strip().lower()
        if input_response == 'yes':
            Doors_opened = 0
        else:
            print("Thanks for playing! See you next time!")
            break