import re


def recursive_method(user_string):
    """Uses a recursive algorithm to determine if a string is a palindrome"""

    print("Recursive method, current string: {}".format(user_string))
    if not len(user_string):
        print("DONE")
        return True
    elif user_string[0] == user_string[-1]:
        print("PASSED!")
        return recursive_method(user_string[1:-1])
    else:
        print("FAILED!")
        return False


def iterative_method(user_string):
    """Uses an iterative algorithm to determine if a string is a palindrome"""

    print("Iterative method...")
    print("Formatting string...")
    user_string = format_string(user_string)

    for letter, other_letter in zip(user_string, user_string[::-1]):
        print("Comparing {} to {}...".format(letter, other_letter))
        if letter is not other_letter:
            print("FAILED!")
            return False
        else:
            print("PASSED!")
    print("DONE!")
    return True


def iterative_method_2(user_string):
    """Iterative method that does not use reverse step on the string."""

    print("Iterative method 2...")
    print("Formatting string...")
    user_string = format_string(user_string)
    count = 0

    while count < len(user_string) / 2:
        print("Comparing {} to {}...".format(user_string[count],
                                             user_string[-1 - count]))
        if user_string[count] is not user_string[-1 - count]:
            print("FAILED!")
            return False
        else:
            print("PASSED!")
        count += 1

    print("DONE!")
    return True


def clever_method(user_string):
    """Quickly determines if a string is a palindrome"""

    if format_string(user_string) == format_string(user_string[::-1]):
        return True
    else:
        return False


def format_string(user_string):
    """Removes all nonalpha characters and converts all letters to lowercase"""

    search_string = re.compile("[^A-Za-z]")
    return re.sub(search_string, '', user_string).lower()


user_input = input("Enter a string: ")

# if clever_method(user_input):
#    print("That is a palindrome.")
# else:
#    print("That is not a palindrome.")

if recursive_method(format_string(user_input)):
    print("That is a palindrome.")
else:
    print("That is not a palindrome.")

# if iterative_method(user_input):
#    print("That is a palindrome.")
# else:
#    print("That is not a palindrome.")

# if iterative_method_2(user_input):
#    print("That is a palindrome.")
# else:
#    print("That is not a palindrome.")
