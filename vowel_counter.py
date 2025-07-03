# Defining a function to count the number of vowels in a string
def count_vowel(string):
    vowels = "aeiouAEIOU" # Giving the computer what vowels are
    count = 0
    for char in string:
        if char in vowels:
            count += 1 # Counting the vowels
    return count

def main():
    strings = str(input("Enter a string: "))
    print(count_vowel(strings), "vowels") # Printing the number of vowels in the string given by the user

# Calling the main function to execute the entire program
main()
