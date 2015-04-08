import re


def normalizing(user_string):
    """Removes all nonalpha characters and converts all letters to lowercase"""
    search_string = re.compile("[^A-Za-z]")
    return re.sub(search_string, '', user_string).lower()


def palindrome(s):
    """Function that determines if the string is a palindrome"""
    if len(s) <= 1:
        return True
    else:
        boolean = s[0] == s[-1] and palindrome(s[1:-1])
        return(boolean)


sentence = input("Please enter your sentence or sentences: ")


if palindrome(normalizing(sentence)):
    print("That is a palindrome")
else:
    print("That is not a palindrome")
