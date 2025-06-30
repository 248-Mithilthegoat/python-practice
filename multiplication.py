def main():
    # Collecting user input
    x = int(input("Enter a number: "))
    # Function for printing multiplication table of x
    multiplication(x)
# Definition of function for printing multiplication table
def multiplication(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)
main()
