
user_string = input('Give me a string, and I shall determine if it is a palindrome. \n>:')

print("Lowering those cases...")
user_string = user_string.lower()
print(user_string)

print("Deleting unwanted characters...")
for iterable in user_string:
    if iterable in "!,;.?":
        user_string = user_string.replace(iterable,'')

print(user_string)

print ("Comparing directions...")

if user_string[::-1] == user_string[:]:
    print ('is a palindrome.')
else:
    print ('is not a palindrome.')
