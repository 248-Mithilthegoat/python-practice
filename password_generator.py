"""
Generating a random password:
Requirements
At least one uppercase letter
At least one lowercase letter
At least one number
At least one special character(!@#$%&*)
At least six characters
Approaches
Create lists and use for loop to pick random options until you meet the character limit

"""
import random

uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase = ["a", "b", "c", "d", "e", "f", "h", "i", "j", "k", "l", "m", "n", "o", "q", "r", "s", "t", "u", "y", "z"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_character = ["!", "@", "#", "$", "%", "^", "&", "*"]
password = random.choice(special_character) + random.choice(number) + random.choice(uppercase)
length = int(input("Enter the length of the password: "))
for _ in range(length - 3):
    password += random.choice(lowercase)

print(password)

