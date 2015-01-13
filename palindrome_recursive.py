import re


def palindrome(words, counter, negative_counter):
    """ Will return if a word is or is not a palindrome """
    if words[counter] != words[negative_counter]:
        print('{} is not the same as {}.'.format(words[counter], words[negative_counter]))
        print('{} is not a palindrome'.format(words))
    elif counter == (len(words) - 1):
        print ('{} is the same as {}.'.format(words[counter], words[negative_counter]))
        print('{} is a palindrome'.format(words))
    else:
        print ('{} is the same as {}.'.format(words[counter], words[negative_counter]))
        counter += 1
        negative_counter -= 1
        palindrome(words, counter, negative_counter)

words = input('Please enter a word: ')
words = re.sub(r'[^A-Za-z]', '', words)
palindrome(words.lower(), 0, -1)
