def show_menu():
    print("1) Rock")
    print("2) Paper")
    print("3) Scissors")
def game():
    show_menu()
    choice = int(input("Make your choice: "))
    import random
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    if choice == 1 and computer_choice == "Rock":
        print("Tie")
    elif choice == 2 and computer_choice == "Rock":
        print("You Win!")
    elif choice == 3 and computer_choice == "Rock":
        print("You Lose!")
    elif choice == 1 and computer_choice == "Paper":
        print("You Lose!")
    elif choice == 2 and computer_choice == "Paper":
        print("Tie")
    elif choice == 3 and computer_choice == "Paper":
        print("You Win!")
    elif choice == 1 and computer_choice == "Scissors":
        print("You Win!")
    elif choice == 2 and computer_choice == "Scissors":
        print("You Lose!")
    elif choice == 3 and computer_choice == "Scissors":
        print("Tie")

def play_again():
    print("Do you want to play again?")
    print("1) Yes")
    print("2) No")
    again = int(input("Make your choice: "))
    if again == 1:
        return True
    return False

def main():
    game()
    play == True
    play = play_again()
    if not play:
        print("Goodbye!")
        pass
    elif play:
        print("Sure!")
        game()

main()
