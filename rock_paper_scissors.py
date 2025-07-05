def show_menu(): # Defining a function to show a menu to the user
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
def game():
    show_menu() # Calling the show_menu() function to show the options to the user
    choice = int(input("Make your choice: "))
    import random # Importing the random function to get access to the function to make the computer pick randomly from options
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    match computer_choice: # Using the match function to create a print statement for every possible case including invalid ones
        case "Rock":
            match choice:
                case 1: 
                    print(f"computer choice: {computer_choice} your choice: rock TIE")
                case 2:
                    print(f"computer choice: {computer_choice} your choice: paper YOU WIN")
                case 3:
                    print(f"computer choice: {computer_choice} your choice: scissors YOU LOSE")
                case _:
                    print("That is not a valid input.")
        case "Paper":
            match choice:
                case 1:
                    print(f"computer choice: {computer_choice} your choice: rock YOU LOSE")
                case 2:
                    print(f"computer choice: {computer_choice} your choice: paper TIE")
                case 3:
                    print(f"computer choice: {computer_choice} your choice: scissors YOU WIN")
                case _:
                    print("That is not a valid input.")
        case "Scissors":
            match choice:
                case 1:
                    print(f"computer choice: {computer_choice} your choice: rock YOU WIN")
                case 2:
                    print(f"computer choice: {computer_choice} your choice: paper YOU LOSE")
                case 3:
                    print(f"computer choice: {computer_choice} your choice: scissors TIE")
                case _:
                    print("That is not a valid input.")

def play_again(): # Defining a function to ask the user if they want to play again
    print("Do you want to play again?")
    print("1) Yes")
    print("2) No")
    again = int(input("Make your choice: "))
    if again == 1:
        return True
    return False

def main():
    play = True
    while play: # Creating a while loop so that if the user wants to play again then it will replay the game
        game()
        play = play_again()
    print("Goodbye!") # Creating a print statement to say "Goodbye!" if the user states that they are done with the game

main()
