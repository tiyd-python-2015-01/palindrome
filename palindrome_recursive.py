import re


def palindrome(words, counter, n_counter):
    """Will return if a word is a palindrome, through a recursive method."""
    if words[counter] != words[n_counter]:
        print('{} is not {}.'.format(words[counter], words[n_counter]))
        print('{} is not a palindrome'.format(words))
    elif counter == (len(words) - 1):
        print('{} is the same as {}.'.format(words[counter], words[n_counter]))
        print('{} is a palindrome'.format(words))
    else:
        print('{} is the same as {}.'.format(words[counter], words[n_counter]))
        counter += 1
        n_counter -= 1
        return palindrome(words, counter, n_counter)

words = input('Please enter a word: ')
words = re.sub(r'[^A-Za-z]', '', words)
print('The program will check the first and last character of the input.')
print('If they are the same it will increment a positive and negative counter.')
print('Then it recalls the function and checks the next character.')
print('If all characters are the same it will tell you its a palindrome.)
print('Anypoint the characters are not the same it will stop.')
palindrome(words.lower(), 0, -1)
