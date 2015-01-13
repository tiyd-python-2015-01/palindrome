import re


def refine_string(input_string):
    """takes a string as input, removes all
       non-alphabetic characters, and changes all letters to lowercase"""
    short_string = re.sub(r'[^A-Za-z]',"", input_string).lower()
    return short_string

def palindrome_iterative(input_string):
    """iterative function to find if input string is a palindrome"""
    short_string = refine_string(input_string)
    halfway_point = len(short_string)/2
    x = 0
    while x < halfway_point:
        if short_string[x] == short_string[-(x+1)]:
            print("testing {}".format(short_string[x]))
            x += 1
        else:
            print("is not a palindrome")
            break
    print("is a palindrome")

def palindrome_recursive(input_string):
    """recursive function to find if input string is a palindrome"""
    short_string = refine_string(input_string)
    halfway_point = len(short_string)/2
    x = 0
    while x < halfway_point:
        if short_string[0] == short_string[len(short_string) - 1]:
            print("testing {}".format(short_string[0]))
            short_string = short_string[1:len(short_string) - 1]
            if len(short_string) <= 1:
                print("is a palindrome")
                break
            return palindrome_recursive(short_string)
        else:
            print("is not a palindrome")
            break


user_input = input("Please enter a palindrome: ")
palindrome_recursive(user_input)
palindrome_iterative(user_input)
