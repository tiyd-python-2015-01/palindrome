import re


def palindrome(words):
    """ Will return if a word is or is not a palindrome """
    counter = -1
    check_word = []
    while not len(check_word) == len(words):
        check_word.append(words[counter])
        print(words, check_word)
        counter -= 1
    check_word = ''.join(check_word)
    print(check_word)
    if words == check_word:
        print('is a palindrome')
    else:
        print('is not a palindrome')

words = input('Please enter a word: ')
words = re.sub(r'[^A-Za-z]', '', words)
palindrome(words.lower)
