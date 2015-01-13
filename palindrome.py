#we need to compare the first index and the last, remove those two and
#repeat.

import re
text = input("Feed me text: ")
original_text = text

def pal2(text):
    lower = (text).lower()
    stripped = re.sub(r'[^A-Za-z]',"", lower)

    if len(stripped) <= 1:
        return "{} is a palindrome.".format(original_text)

    elif stripped[0] == stripped[-1]:
        text1 = stripped[1:-1]
        return pal2(text1)


    elif text[0] != text[-1]:
        return ("This is not a palindrome.")



print(pal2(text))
