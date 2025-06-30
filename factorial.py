# Defining function to collect user input and validate and return the validation
def get_input():
    x = int(input("Enter a positive integer: "))
    if x < 0:
        return False, x
    return True, x


# Defining function to implement the factorial on the number given by the user and then returning that value
def factorial_implementation(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial

# Main function with all functions
def main():
    is_valid = False

    while(not is_valid):
        is_valid, x = get_input()
        if not is_valid:
            print(f"{x} is not positive.")
    result = factorial_implementation(x)
    print(x, "factorial =", result)


# Executing the main function to execute the entire program
main()

