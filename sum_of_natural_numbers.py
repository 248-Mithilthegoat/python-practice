def main():
    is_valid == True
    # Collecting user input
    x = int(input("Enter a number: "))
    # Checking if input is valid, and if not printing a message accordingly
    get_input(x)
    # Executing a function to add the natural numbers consecutively
    if is_valid is False:
        pass
    elif is_valid is True:
        sum_natural_numbers(x)
# Defining the function to check if the number given by the user is valid
def get_input(n):
    # Conditional to print a message if the user input is invalid
    
    if n <= 0:
        print("Enter a number greater than 0. ")
        return is_valid is False
    elif n > 0:
        return n
# Defining the function to add the natural nubers consecutively
def sum_natural_numbers(a):
    sum = 0
    for i in range(1, a+1):
        sum += i
    print(sum)
# Executing the entire program
main()
