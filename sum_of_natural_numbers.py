def get_input():
    x = int(input("PLease enter a positive integer: "))
    if x < 0:
        return False, x
    return True, x



def sum_of_numbers(x):
    sum = 0
    for i in range(1, x+1):
        sum += i
    return sum


def main():
    is_valid = False
    while(not is_valid):
        is_valid, x = get_input()
        if not is_valid:
            print(f"{x} is not a positive integer")
        
    result = sum_of_numbers(x)
    print(f"The sum of {x} natural numbers is {result}")
main()
