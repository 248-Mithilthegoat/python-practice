import random # Importing the random.choice function
a = range(1, 101) # Creating a variable with the range of 1-100
def guess(choice):
    num = int(input("Guess a number from 1-100: ")) # Using if and elif statements to tell the user if they need to guess higher or lower or if they got it right
    if num < choice:
            print("Higher")
            return False
    elif num > choice:
            print("Lower")
            return False
    elif num == choice:
            print("You did it!")
            return True

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
    while play: # Using a while loop to repeatedly ask the user until they guess the right number and ask if they want to play again or not
        correct = False
        attempts = 0
        choice = random.choice(a)
        while not correct:
            correct = guess(choice)
            attempts += 1
        print(f"{attempts} attempts")
        play = play_again()
main()
