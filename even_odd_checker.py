def main():
    # Collect user input
    x = int(input("Enter a number: "))
    # Checking if even or odd
    even_odd_checker(x)
def even_odd_checker(n):
    if n%2== 0:
        print(n,"is even.")
    else:
        print(n,"is odd.")
main()
