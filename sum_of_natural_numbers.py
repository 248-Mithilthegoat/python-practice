def main():
    # Collecting user input
    x = int(input("Enter a number: "))
    sum_natural_numbers(x)

# Loop that continuously adds down to 0
def sum_natural_numbers(n):
    sum = 0
    for i in range(1, n+1):
        # Changes the value of sum variable to the sum of the natural numbers
        sum += i
    print(sum)
main()
