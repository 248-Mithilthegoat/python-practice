def main():
    x = int(input("Enter number x: "))
    y = int(input("Enter number y: "))
    operator = str(input("Enter the operator: "))
    calculate(x, y, operator)
def calculate(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print(num1 / num2)
        elif num2 == 0:
            print("Divide by zero error")
main()
