def get_input():
    x = int(input("Enter a positive integer: "))
    if x < 0:
        return False, x
    return True, x
even = "even"
odd = "odd"
y = None
def even_odd_checker(x):
    if x % 2 == 0:
        y = "even"
    else:
        y = "odd"
    return y



def main():
    is_valid = False

    while(not is_valid):
        is_valid, x = get_input()

        if (not is_valid):
            print(f"{x} is not a positive integer")
    print(f"{x} is {y}")


main()
