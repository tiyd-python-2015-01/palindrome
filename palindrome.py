import re


def palindrome(words):
    """ Will return if a word is or is not a palindrome """
    print("The computer is comparing the original string with the reverse of the string.")
    if words[::-1] == words:
        print("is a palindrome")
    else:
        print("is not a palindrome")

words = input("Please enter a word: ")
words = re.sub(r'[^A-Za-z]', '', words)
palindrome(words.lower())
