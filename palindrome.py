def preprocess(sentence):
    sentencelist=[]
    for letters in sentence:
        if letters.isalpha():
            sentencelist.append(letters)
    return sentencelist

print("I will check if the sentence you enter is a palindrome")
sentence = input("Enter a Sentence ")
sentence=preprocess(sentence.lower())
newsentence=[]

for letters in sentence[::-1]:
    newsentence.append(letters)

if list(sentence) == newsentence:
    print("YES!!!!!!  It is a palindrome")
else:
    print("NO!!!!  It is not a palindrome")
