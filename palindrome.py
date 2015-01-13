import re

print("Let's see if you have a palindrome!")
guess = str(input("> "))

string_low = guess.lower()
print(string_low)

string_clean = re.sub(r'[^A-Za-z]', '', string_low)
print (string_clean)

string_reverse = string_clean[::-1]
print(string_reverse)

if string_clean == string_reverse:
    print("{} is a palindrome!".format(guess))
else:
    print("{} is not a palindrome!".format(guess))
