# Collecting user input
x = input("Enter a string: ").strip()
# Creating lists for all categories
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sentence_breakers = ["!", ".", "?"]
vowels = ["a", "e", "i", "o", "u"]
word_breakers = " "
sentence_count = 0
vowel_count = 0
word_count = 0
character_count = 0
for value in x: # Using for loops and if conditionals to add to the counts
    if value in word_breakers:
        word_count += 1
        character_count += 1
    if value in vowels:
        vowel_count += 1
    if value in sentence_breakers:
        sentence_count += 1
    if value in characters:
        character_count += 1

print(f"The vowel count is {vowel_count}.")
print(f"The word count is {word_count + 1}.")
print(f"The character count is {character_count}.")
print(f"The sentence count is {sentence_count}.")