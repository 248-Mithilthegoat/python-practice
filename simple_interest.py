principal = int(input("Enter the principal amount: ")) # Collecting the principal amount
interest_rate = float(input("Enter the interest rate: ")) # Collecting the interest rate per year
time = int(input("Enter how many years the deposit has been in the account: ")) # Collecting the time that the principal has been in the account
def check_input(x):
    if x < 0:
        return False, x
    return True, x
def main():
    principal = int(input("Enter the principal amount: ")) # Collecting the principal amount
    interest_rate = float(input("Enter the interest rate: ")) # Collecting the interest rate per year
    time = int(input("Enter how many years the deposit has been in the account: ")) # Collecting the time that the principal has been in the account
    is_valid = False
    check_input(principal)
    while not is_valid:
        print("That is not a valid principal.")
        principal = int(input("Enter the principal amount: "))
    check_valid = False
    check_input(interest_rate)
    while not check_valid:
        print("That is not a valid interest rate.")
        interest_rate = float(input("Enter the interest rate: "))
    isn_valid = False
    check_input(time)
    while not isn_valid:
        print("That is not a valid time.")
        time = int(input("Enter how many years the deposit has been in the account: "))
        simple_interest = 0
    simple_interest = (principal * interest_rate * time) / 100 # Calculating the simple interest
    print(f"The simple interest is ${simple_interest}. The total amount is ${principal + simple_interest}.") # Printing the simple interest and the total the deposit is worth
main()