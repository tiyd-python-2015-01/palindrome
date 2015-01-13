import re

first_word = input("Please enter a word to see if it's a palindrome. ")

new_first_word = re.sub(r'[^A-Za-z]', '', first_word).lower()

def palindrome_recursion(word, start_num = 0, end_num = -1):
    """Pass in a word to determine if it's a palindrome recursively."""
    start_letter = word[start_num]
    print(start_num)

    end_letter = word[end_num]
    print(abs(end_num))

    if abs(end_num) == len(word):
        print("{} is a palindrome.".format(first_word))
        quit()

    if start_letter == end_letter:
        start_num += 1
        end_num -= 1
        palindrome_recursion(word, start_num = start_num,
        end_num = end_num)

    else:
        print("{} is not a palindrome.".format(first_word))

def palindrome_simple(word):
    """Pass in a word to determine if it's a palindrome"""

    new_first_word = re.sub(r'[^A-Za-z]', '', first_word).lower()
    print(new_first_word)

    inverse = new_first_word[::-1]
    print(inverse)

    if new_first_word == inverse:
        print("{} is a palindrome.".format(first_word))
    else:
        print("{} is not a palindrome.".format(first_word))

palindrome_recursion(new_first_word)
