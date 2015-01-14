strip_characters = [" ", "'", ",", ".", "-", "+", ":", ";", "!"]


def pal():

    user_input = input("Enter a sentence, and I'll check if "
                       "it's a palindrome: ")

    reverse = (user_input[::-1])

    for characters in strip_characters:
        reverse = reverse.replace(characters, "").lower()
        user_input = user_input.replace(characters, "").lower()

    if reverse == user_input:
        print("This is a palindrome.")
    else:
        print("This is not a palindrome.")

pal()
