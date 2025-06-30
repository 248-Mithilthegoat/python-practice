# Defining the function to collect user input(x) and check if it is valid, then return the value and whether or not the user input is valid
def get_input():
    x = int(input("Enter a positive number: "))
    
    if x < 0:
        return False, x
    return True, x


# Main program to execute all functions
def main():
    is_valid = False

    # While loop to print a message and ask for a different number if the given number is invalid
    while(not is_valid):
        is_valid, x = get_input()
        if (not is_valid):
            print(f"{x} is not a positive number.")
    # For loop that prints the multiplication table
    for i in range(1, 11):
        print(x, "x", i, "=", x*i)

# Executing the entire program
main()
