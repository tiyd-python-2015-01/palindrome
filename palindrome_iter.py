import re

def pal():
    original_word = input("Gimme a word or sentence: ") #Ask for word input
    lower_word = original_word.lower() #take word input and use .lower()
    strip_word = re.sub(r'[^A-Za-z]', "", lower_word)
    print(lower_word)
    print(strip_word)
    front_index = 0
    end_index = -1

    for letter in strip_word:
        if strip_word[front_index] == strip_word[end_index]:
            #print(lower_word[front_index],lower_word[end_index])
            front_index += 1
            end_index -= 1
        else:
            return "This is not a palindrome"
    return "{} is a palindrome".format(original_word)

print(pal())



#working with Ben & Joel & Zach
