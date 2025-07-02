# Defining a function to reverse a given string
def string_reverser():
    string = str(input("Enter a string to be reversed: "))
    reversed_string = "".join(reversed(string)) # Function to reverse the string
    print(reversed_string)

def main():
    string_reverser() # Calling the string_reverser function


# Calling the main function to execute the entire program
main()
