def main():
    x = int(input("Enter a number: "))
    get_input(x)
    sum_natural_numbers(x)
def get_input(n):
    if n <= 0:
        n =int(input("Enter a number greater than 0: "))
    elif n > 0:
        return n
def sum_natural_numbers(a):
    sum = 0
    for i in range(1, a+1):
        sum += i
    print(sum)
main()
