import random
a = range(1, 101)
choice = random.choice(a)
def guess():
    num = int(input("Guess a number from 1-100: "))
    attempts = 0
    import repeat
    if num < choice:
        print("Higher")
        attempts += 1
        repeat(guess())
    elif num > choice:
        print("Lower")
        attempts += 1
        repeat(guess())
    elif num == choice:
        print("You did it!")
        print(attempts, "attempts.")
def main():
    guess()
main()