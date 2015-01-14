'''
Still needs closure, output, and prints. Needs To Use "is a palindrome" and "is not a palindrome" at closure

Could use the following for normalize:

def remove(s):
        sentence = re.sub(r'[^A-Za-z]', '',sentence)
        return sentence
'''



sentence = input("Please enter your sentence or sentences: ")

print("Removing characters. Lowering cases...")

def overseer(s):

    def normalizing(s):
        """converting characters to ascii and alphanumeric letters"""
        return u"".join(i if isPlainASCIIAlphaNum(i) else '' for i in s)
        #could use re.sub here

    def lowering_case(s):
        return s.lower()

    def palindrome(s):
        if len(s) <= 1:
            return True
        else:
            boolean = s[0] == s[-1] and palindrome(s[1:-1])
            return(boolean)

    return palindrome(normalize(s))

return sentence
