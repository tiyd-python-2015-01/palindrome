
def pal():
    """Compares"""
    original_word = input("Gimme a word or sentence: ") #Ask for word input
    lower_word = original_word.lower() #take word input and use .lower()
    #print(lower_word)
    #strip out puncuation and spaces
    if lower_word == lower_word[::-1]:
        print("{} is a palindrome".format(original_word))
    else:
        print("{} is NOT a palindrome".format(original_word))

print(pal())




#working with Ben & Joel
