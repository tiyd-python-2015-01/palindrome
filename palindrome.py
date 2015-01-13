strip_characters = [" ", "'", ",", ".", "-", "+"]


def check_my_pal():

    user_input = input("Enter a sentence, "
                       "and I'll check if it's a palindrome:> ")

    for characters in strip_characters:
        user_input = user_input.replace(characters, "").lower()

    if user_input.isalpha():

        print("Taking out characters and compressing the sentence...")
        print("Compressed sentence = {}".format(user_input))

        def pal_recur(sentence):
            if len(sentence) < 2:
                print("=="*20)
                print("It's a palindrome")
                return True

            if sentence[0] != sentence[-1]:
                print("It's not a palindrome")
                return False

            print("Comparing parrallel characters: {}{}{}".format('\x1b[1;31m'
                  + sentence[0] + '\x1b[0m', sentence[1:-1], '\x1b[1;31m' +
                  sentence[-1] + '\x1b[0m'))

            return pal_recur(sentence[1:-1])
        pal_recur(user_input)
    else:
        print("Enter an alpha character ya dingus.")
        check_my_pal()

check_my_pal()


# Here's the non recursive solution!

strip_characters = [" ", "'", ",", ".", "-"]


def pal():

    user_input = input("Enter a sentence, and I'll check if "
                       "it's a palindrome: ")

    reverse = (user_input[::-1])

    for characters in strip_characters:
        reverse = reverse.replace(characters, "").lower()
        user_input = user_input.replace(characters, "").lower()

    if reverse == user_input:
        print("It's a palindrome!!")
    else:
        print("It's not a palindrome!!")

pal()
#
#
#
#  print("Breakin' down the smushed sentence: {}".format(sentence[1:-1]))
