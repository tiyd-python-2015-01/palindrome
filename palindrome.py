#Jason Aylward
#January 13, 2015
#Homework 2

def clean_up(original_text):
    """Removes punctuation and lowercases all letters"""
    lower_text = original_text.lower()
    new_text = []
    for character in lower_text:
        if character.isalpha():
            new_text.append(character)
    return ''.join(new_text)

def rec_palindrome(input_word, leftside_place):
    """function will iterate through a phrase from the outside in
    and return FALSE if any compared character is found different
    between the front half and the back half.
    IF the leftside_place passes half the input_word, it means all the characters
    have been passed"""
    if leftside_place > (len(input_word)//2):
        return True
    rightside_place = len(input_word) - leftside_place - 1
    if input_word[leftside_place] == input_word[rightside_place ]:
        print("Recursively checking characters at {} and {} to see if they are equal.\nCharacters are {} and {}".format(leftside_place,rightside_place,input_word[leftside_place],input_word[rightside_place]))
        return rec_palindrome(input_word,leftside_place+1)
    return False

def iter_palindrome(input_word):
    """Iteratively traverses input_word, checking from the outside in
    IF a character on the left is NOT EQUAL to a character on the right, return FALSE
    ELSE return TRUE after passing the halfway mark"""
    place_count = 0
    while place_count < len(input_word)//2:
        print("Left ",input_word[place_count])
        print("Right ", input_word[(-place_count)-1])
        print("Iteratively checking characters at {} and {} to see if they are equal.\nCharacters are {} and {}".format(place_count,len(input_word)-place_count-1,input_word[place_count],input_word[-place_count-1]))
        if input_word[place_count] != input_word[-place_count-1]:
            return False
        place_count +=1
    return True

user_input = input("Please enter a possible palindrome: ")
clean_input = clean_up(user_input)

if iter_palindrome(clean_input):
#if rec_palindrome(clean_input,0):
    print("Yes, {} is a palindrome".format(user_input))
else:
    print("No, {} is not a palindrome.".format(user_input))
