# Defining a function called palindrome checker
def palindrome_checker():
    string = str(input("Enter a string: "))
    stripped_string = string.replace(" ", "").lower() # Function to replace all spaces and lowercase
    reversed_string = ''.join(reversed(stripped_string)) # Function to reverse the string
    if stripped_string == reversed_string: # If condition to check if the string is a palindrome or not
        print(f"{string} is a palindrome.")
    else:
        print(f"{string} is not a palindrome.")

def main():
    palindrome_checker() # Calling the palindrome checker function to check if the string given by the user is a palindrome

# Calling the main function to execute entire program
main()

