import re

def pal(word):
    if len(word) <= 1:
        return True
    elif word[0] == word[-1]:
        new_word = word[1:-1]
        return pal(new_word)
    else:
        return False

original_word = input("Gimme a word or sentence: ") #Ask for word input
lower_word = original_word.lower() #take word input and use .lower()
strip_word = re.sub(r'[^A-Za-z]', "", lower_word)
#print(lower_word)
#print(strip_word)
if pal(strip_word) == True:
    print("{} is a palindrome, hooray!!!".format(original_word))
elif pal(strip_word) == False:
    print("{} is NOT palindrome, sorry".format(original_word))
