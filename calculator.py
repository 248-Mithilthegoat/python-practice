def main():
   # Getting user input for the two numbers and operator
    x = int(input("Enter number x: "))
    y = int(input("Enter number y: "))
    operator = str(input("Enter the operator: "))
    calculate(x, y, operator)
def calculate(num1, num2, operator):
    # Checking which operator and continuing with that operation
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        # Checking if there is a division by zero, and if so printing "Divide by zero error"
        if num2 != 0:
            print(num1 / num2)
        elif num2 == 0:
            print("Divide by zero error")
main()
