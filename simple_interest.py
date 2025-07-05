def check_input(x): # Defining the function to check if user input is valid
    if x < 0: 
        return False
    return True
def main():
    is_principal_valid = False
    is_interest_valid = False
    is_term_valid = False
    while not is_principal_valid: # While loops and if conditionals to check if user inputs are valid or not
        principal = int(input("Enter the principal amount: "))
        is_principal_valid = check_input(principal)
        if not is_principal_valid:
            print("Principal that you entered is not valid!")
    while not is_interest_valid:
        interest_rate = float(input("Enter the interest rate: "))
        is_interest_valid = check_input(interest_rate)
        if not is_interest_valid:
            print("Interest that you entered is not valid")
    while not is_term_valid:
        time = int(input("Enter how many years the deposit has been in the account: "))
        is_term_valid = check_input(time)
        if not is_term_valid:
            print("Time is not valid")
    simple_interest = (principal * interest_rate * time) / 100 # Calculating the simple interest
    print(f"The simple interest is ${simple_interest}. The total amount is ${principal + simple_interest}.") # Printing the simple interest and the total the deposit is worth
main()