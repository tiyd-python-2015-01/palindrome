import re

print("Let's see if you have a palindrome!")
guess = str(input("> "))

string_low = guess.lower()
print(string_low)

string_clean = re.sub(r'[^A-Za-z]', '', string_low)
print (string_clean)


def trim(string_clean):
    """A recursive function which compares and trims the beginning and ends
    of a clean string to determine whether it is a palindrome"""

    if len(string_clean) > 1:
        if string_clean[0] == string_clean[-1]:
            return trim(string_clean[1:-1])
        else:
            return False
    else:
        return True

def iter_trim(string_clean):
    """An iterative function which compares and trims the beginning and ends
     of a clean string to determine whether it is a palindrome"""
    str_length = len(string_clean)
    while str_length > 1:
        if string_clean[0] == string_clean[-1]:
            string_clean = string_clean[1: -1]
            str_length = str_length -2
        else: return False
    return True

if trim(string_clean):
    print("{} is a palindrome!".format(guess))
else:
    print("{} is not a palindrome!".format(guess))
