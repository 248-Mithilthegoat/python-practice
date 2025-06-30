# Main code
def main():
    # Getting user input
    x = int(input("Enter a number: "))
    # Factorial function
    factorial_implementation(x)

# Definition of factorial implementation function
def factorial_implementation(n):
    factorial = 1
    # Loop that causes the given number to multiply continuously
    for i in range(1, n+1):
        factorial = factorial*i
    print(factorial)
# Executing the program
main()

