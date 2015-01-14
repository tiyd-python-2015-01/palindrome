my_str = input("Enter a sentence to find out if it is a palindrome")

strip_characters(" ",".",",","-","?")
replace_characters with ("")

def ispalindrome(sentence):
    if len(sentence) < 2:
        print("Is a palindrome")
        return True


    if sentence[0] != sentence[-1]:
        print("Is not a palindrome")
        return False
    return ispalindrome(sentence[1:-1])

ispalindrome("anna")


#-------------------------------------


#I tried to figure out how to put """str.strip([" ","."",","!","?"]);"""
my_str = input("Enter a Sentence: ")

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not a palindrome")
