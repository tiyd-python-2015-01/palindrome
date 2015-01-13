import re

def palindrome(words):
    """Will return if a word is a palindrome, through an iterative method."""
    words = re.sub(r'[^A-Za-z]', '', words)
    counter = -1
    check_word = []
    print("The function will create a new list of characters")
    print("by appending the last character of the string, and moving backward.")
    while not len(check_word) == len(words):
        print('{} was appended'.format(words[counter]))
        check_word.append(words[counter])
        counter -= 1
    check_word = ''.join(check_word)
    print('The reverse of the given word is {}'.format(check_word))
    if words == check_word:
        print('is a palindrome')
    else:
        print('is not a palindrome')

words = input('Please enter a word: ')
palindrome(words.lower())
