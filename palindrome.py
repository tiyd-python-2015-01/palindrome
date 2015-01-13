import re

first_word = input("Please enter a word to see if it's a palindrome ")

new_first_word = re.sub(r'[^A-Za-z]', '', first_word).lower()

print(new_first_word)

inverse = new_first_word[::-1]
print(inverse)

if new_first_word == inverse:
    print("{} is a palindrome.".format(first_word))
else:
    print("{} is not a palindrome.".format(first_word))
