strip_characters = [" ", "'", ",", ".", "-", "+", ":", ";", "!"]


def check_my_pal():

    user_input = input("Enter a sentence, "
                       "and I'll check if it's a palindrome: ")

    for characters in strip_characters:
        user_input = user_input.replace(characters, "").lower()

    if user_input.isalpha():

        print("Taking out characters and compressing the sentence...")
        print("Compressed sentence = {}".format(user_input))

        def pal_recur(sentence):
            if len(sentence) < 2:
                print("=="*20)
                print("This is a palindrome")
                return True

            if sentence[0] != sentence[-1]:
                print("This is not a palindrome")
                return False

            print("Comparing mirrored characters: {}{}{}".format('\x1b[1;31m'
                  + sentence[0] + '\x1b[0m', sentence[1:-1], '\x1b[1;31m' +
                  sentence[-1] + '\x1b[0m'))

            return pal_recur(sentence[1:-1])
        pal_recur(user_input)
    else:
        print("Enter alpha characters ya dingus.")
        check_my_pal()

check_my_pal()
