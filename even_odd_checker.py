# Defining the get_input function to return whether the given input is valid or invalid
def get_input():
    x = int(input("Enter a positive integer: "))
    if x < 0:
        return False, x
    return True, x
# Defining the function to check whether the given number is even/odd and returning that answer
def even_odd_checker(x):
    if x % 2 == 0:
        y = "even"
    else:
        y = "odd"
    return y



# The main function that holds the entire execution
def main():
    is_valid = False

    # While loop that if the given number is invalid, will print a message and ask for a different number
    while(not is_valid):
        is_valid, x = get_input()

        if (not is_valid):
            print(f"{x} is not a positive integer")
    # Executing the function to check if x is even/odd
    y = even_odd_checker(x)
    print(f"{x} is {y}")


# Executing the entire program
main()
