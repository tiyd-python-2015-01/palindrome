def palindrome(user_string):
    if len(user_string) <= 1:
        return True
    elif user_string[0] == user_string[-1]:
        new_string = palindrome(user_string[1:-1])
        return new_string
    else:
        return False

user_string = input('Give me a string, and I shall determine if it is a palindrome. \n>:')

print("Lowering those cases...")
user_string = user_string.lower()
print(user_string)

print("Deleting unwanted characters...")
for iterable in user_string:
    if iterable in "!,;.?":
        user_string = user_string.replace(iterable,'')

if palindrome(user_string) == True:
    print ('is a palindrome.')
else:
    print ('is not a palindrome.')

# Zach and Lee were big a help with recursion
