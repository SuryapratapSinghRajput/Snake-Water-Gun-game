print("-------------SNAKE-WATER-GUN-----------------")
import random
def game():
    # 1:snake ,2:Gun ,-1:Water
    choices = (1,2,-1)
    computer = random.choice(choices)
    try:
         your_choice = int(input("choose one character \n 1:Snake \n 2:Gun \n -1:Water \n your choice: "))
    except ValueError:
        print("Invalid input! please enter a number (1,2,-1).")
        return
    #check for a tie game
    if computer == your_choice:
        print("Draw")
    #player winning condition

    elif  computer == 1 and your_choice == 2:
        print("you Won")
    elif  computer == 2 and your_choice == -1:
        print("You Won")
    elif  computer == -1 and your_choice == 1:
        print("You Won")
    #Computer winning condition
    elif  computer == 2 and your_choice == 1:
        print("computer Won")
    elif  computer == 1 and your_choice == -1:
        print("computer  Won")
    elif  computer == -1 and your_choice == 2:
        print("computer  Won")
    else:
        print("invalid choice")
#main game loop to keep the game running
while True:

    game()
    #check if the player wants to play another round
    play_again = input("Do you wanna play another round (y|n)").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")  
        break    


