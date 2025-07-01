# Collecting user input
x = int(input("Enter the temperature: "))
# Creating a function to print a menu, get the choice from the user, validate, and return the validation and value
def get_menu_input():
    print("1) Fahrenheit to Celsius")
    print("2) Celsius to Fahrenheit")
    choice = int(input("Make your choice: "))
    if choice == 1 or choice == 2:
        return True, choice
    return False, choice
def main():
    is_valid = False
    while(not is_valid): # While loop that if the user input is invalid will print a message and ask the user again
        is_valid, choice = get_menu_input()
        if not is_valid:
            print("Choose one of the options 1 or 2.")
    if choice == 1:
        C = 0
        C = (x - 32) * 5/9 # Formula for converting Fahrenheit to Celsius
        C = round(C) # Function to round the output to the nearest integer
        print(C, "degrees")
    elif choice == 2:
        F = 0
        F = (x * 9/5) + 32 # Formula for converting Celsius to Fahrenheit
        F = round(F) # Function to round the output to the nearest integer
        print(F, "degrees")

# Executing the main function to execute the entire program
main()
