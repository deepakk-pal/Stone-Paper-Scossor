#Importing Random module to choose random action by computer..
import random 

while True:

    #Taking user Input
    user_input = input("Please enter your among (Stone, Paper, Scissor) : ")

    #Set of chances/Actions
    possible_choices = ['Rock', 'Paper', 'Scissor']

    #from this computer will make a random choice from the chpices given above
    computer_choice = random.choice(possible_choices)
    print(f'Your chooice is {user_input}\nComputers choice is {computer_choice}')

    #Deciding Champion 

    if user_input == computer_choice:
        print(f"Ohh it's a tie!! ")

    elif user_input=="Stone":
        if computer_choice == "Paper":
            print("Paper covers Stone! You Lost")
        else:
            print("Stone trashes scissors ! You Win")

    elif user_input=="Paper":
        if computer_choice == "Scissor":
            print("Scissors cut the paper !! You Lost")
        else:
            print("Paper covers the stone!! You Win")

    elif user_input=="Scissor":
        if computer_choice == "Paper":
            print("Scissor cut the paper!! Yow Win ")
        else:
            print("Stone Trashes scissors!! You Lost")
            

     #Asking the player whether layer want to play again or not!!       
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
