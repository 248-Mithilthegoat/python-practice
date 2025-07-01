def get_input():
    a = int(input("Enter a positive integer: "))
    if a <= 1:
        return False, a
    return True, a

def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            print(n, "is composite")
            break
    else:
        print(n, "is prime")

def main():
    is_valid = False
    while(not is_valid):
        is_valid, a = get_input()
        if not is_valid:
            print(a, "is not greater than 1.")
    check_prime(a)

main()
