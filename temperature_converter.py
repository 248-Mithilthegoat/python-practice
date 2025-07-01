# Defining the function to show the options to the user
def show_menu():
    print("1) Fahrenheit to Celsius")
    print("2) Celsius to Fahrenheit")

# Collecting user input
x = int(input("Enter the temperature: "))

# The main function with all other functions(excluding the function to collect user input)
def main():
    # Executing the function to print the options for the user
    show_menu()
    choice = int(input("Make your choice: ")) # Collecting user input of which format, Fahrenheit to Celsius or Celsius to Fahrenheit
    # Function for what to do if the user inputs Fahrenheit to Celsius
    if choice == 1:
        C = 0
        C = (x - 32) * 5/9 # Formula for converting Fahrenheit to Celsius
        C = round(C, 2)
        print(C, "degrees")
    # Function for what to do if the user inputs Celsius to Fahrenheit
    elif choice == 2:
        F = 0
        F = (x * 9/5) + 32 # Formula for converting Celsius to Fahrenheit
        F = round(F, 2)
        print(F, "degrees")

# Executing the main function to execute the entire program
main()