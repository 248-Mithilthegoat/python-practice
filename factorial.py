def get_input():
    x = int(input("Enter a positive integer: "))
    if x < 0:
        return False, x
    return True, x


def factorial_implementation(x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i
    return factorial

def main():
    is_valid = False

    while(not is_valid):
        is_valid, x = get_input()
        if not is_valid:
            print(f"{x} is not positive.")
    result = factorial_implementation(x)
    print(x, "factorial =", result)


main()

