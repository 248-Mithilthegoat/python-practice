import random
a = range(1, 101)
def guess():
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
def play_again():
    print("Do you want to play?")
    print("1) Yes")
    print("2) No")
    again = int(input("Make your choice: "))
    if again == 1:
          return True
    return False
def main():
    play = True
    while play:
          correct = False
          attempts = 0
          choice = random.choice(a)
          while not correct:
                correct = guess()
                
                

main()
