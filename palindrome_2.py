#we need to compare the first index and the last, remove those two and
#repeat.

import re
text = input("Feed me text: ")

def pal2(text):
    #print("user", text)
    lower = (text).lower()
    #print (lower)
    stripped = re.sub(r'[^A-Za-z]',"", lower)
    #print (stripped)

    if len(stripped) == 1:
        return "This is a palindrome."

    elif stripped[0] == stripped[-1]:
        text1 = stripped[1:-1]
        #print ("loop", text1)
        return pal2(text1)


    elif text[0] != text[-1]:
            print ("This is not a palindrome.")

pal2(text)  
