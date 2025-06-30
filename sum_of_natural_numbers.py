# Defining function to collect input from user and validate
def get_input():
    x = int(input("Please enter a positive interger: "))
    if x < 0:
        # Returning whether the input is valid or invalid
        return False, x
    return True, x


# Defining the function to add the numbers continuously and return the final sum
def sum_of_numbers(x):
    sum = 0
    for i in range(1, x+1):
        sum += i
    return sum

# Main function which holds program
def main():
    is_valid = False
    # While loop that prints a message and asks for another number if the given number is invalid
    while(not is_valid):
        is_valid, x = get_input()
        if not is_valid:
            print(f"{x} is not a positive integer")
        
    # Printing the sum of x natural numbers
    result = sum_of_numbers(x)
    print(f"The sum of {x} natural numbers is {result}")
# Executing the entire program
main()
