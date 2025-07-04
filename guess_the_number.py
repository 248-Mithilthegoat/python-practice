import random # Importing the random function to have access to random.choice
a = range(1, 101) # Creating a variable with a range of 1 - 100
def guess(choice): # Defining a function to print whether the users guess needs to be higher or lower or if it is correct
    num = int(input("Guess a number from 1-100: "))
    if num < choice:
            print("Higher")
            return False
    elif num > choice:
            print("Lower")
            return False
    elif num == choice:
            print("You did it!")
            return True
def play_again(): # Defining a function to ask if the user wants to play again
    print("Do you want to play again?")
    print("1) Yes")
    print("2) No")
    again = int(input("Make your choice: "))
    if again == 1:
          return True
    return False
def main():
    play = True
    while play: # Creating a while loop to ask if the user wants to play again, if they do then it will restart the game, if they don't then it will simply stop
        correct = False
        attempts = 0
        choice = random.choice(a)
        while not correct:
            correct = guess(choice)
            attempts += 1
        print(f"{attempts} attempts")
        play = play_again()
main()
