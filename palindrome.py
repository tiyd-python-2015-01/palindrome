import re


def palindrome(words):
    """Will return if a word is a palindrome."""
    print("Comparing the original string with the reverse of the string...")
    if words[::-1] == words:
        print("The string reversed was the same as the normal string!")
        print("is a palindrome")
    else:
        print("The string reversed was not the same as the normal string.")
        print("is not a palindrome")

words = input("Please enter a word: ")
words = re.sub(r'[^A-Za-z]', '', words)
palindrome(words.lower())
