principal = int(input("Enter the principal amount: ")) # Collecting the principal amount
interest_rate = float(input("Enter the interest rate: ")) # Collecting the interest rate per year
time = int(input("Enter how many years the deposit has been in the account: ")) # Collecting the time that the principal has been in the account
simple_interest = 0
simple_interest = (principal * interest_rate * time) / 100 # Calculating the simple interest
print(f"The simple interest is ${simple_interest}. The total amount is ${principal + simple_interest}.") # Printing the simple interest and the total the deposit is worth