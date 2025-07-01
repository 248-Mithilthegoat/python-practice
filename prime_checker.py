# Defining function to collect input and validate and return the value of a and validation
def get_input():
    a = int(input("Enter a positive integer: "))
    if a <= 1:
        return False, a
    return True, a

# Definition of check_prime function to check if a given number is prime/composite
def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            print(n, "is composite")
            return
    print(n, "is prime.")

# The main program with all functions
def main():
    is_valid = False
    while(not is_valid):
        is_valid, a = get_input()
        if not is_valid:
            print(a, "is not greater than 1.")
    check_prime(a)

# Executing the main function to execute the entire program
main()
