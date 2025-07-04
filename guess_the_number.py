import random
a = range(1, 101)
choice = random.choice(a)
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
            correct = True
            return True
def main():
    correct = False
    attempts = 0
    while (not correct):
        attempts += 1
        guess()
    print(attempts)
main()
