def main():
    # Collect user input
    x = int(input("Enter a number: "))
    # Function to check if user input is valid, if invalid prints a message
    get_input(x)
    # Function to check if user input is even/odd
    even_odd_checker(x)
# Defining the function to check for invalid input and if input is invalid printing a message
def get_input(a):
    if a <= 0:
        print("Enter a number greater than 0")
    elif a > 0:
        return a
# Defining a function to check if the number given by the user is even/odd
def even_odd_checker(n):
    if n%2== 0:
        print(n,"is even.")
    else:
        print(n,"is odd.")
main()
