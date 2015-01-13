def pal():

    word = input("Give me a word to see if its a palindrome:")

    print("First I make the word lower case...")
    word = word.lower()

    print(word)
    print("Next I take out punctuation and spaces...")

    for character in " !?,":
        word = word.replace(character, "")

    print(word)
    print("Now to see if it's a palindrome...")

    if word == word[::-1]:
        return "This is a pallindrome"
    else:
        return "This is not a pallindrome"

    return word

print(pal()) 
