import re

punctuation = re.compile(r'[^A-Za-z]')

user_input = input("Give me a string and I'll see if it's a palindrome: ")

def is_palindrome(potential_palindrome):
	"""Inspects a string of lowercase letters to assess if the string
	is a palindrome. Returns a boolean"""
	print("Now considering: '{}''".format(potential_palindrome))

	if len(potential_palindrome) > 1:
		print("It's longer than one character!")
		if not potential_palindrome[0] == potential_palindrome[-1]:
			print("But the ends don't match! False!")
			return False
		else:
			print("The ends match!")
			if len(potential_palindrome) == 2:
				print("And that's all of it! It must be a palindrome!")
				return True
			else:
				print("So, that just leaves the rest of the string...")
				return is_palindrome(potential_palindrome[1:-1])
	else:
		print("It's just one character! True!")
		return True

def iterative_palindrome(potential_palindrome):
	front_pointer = 0
	back_pointer = -1
	counter = len(potential_palindrome)
	while counter > 0:
		if not potential_palindrome[front_pointer] == potential_palindrome[back_pointer]:
			return False
		else:
			front_pointer += 1
			back_pointer -= 1
			counter -= 2
	return True


clean_string = punctuation.sub("", user_input)
clean_string = clean_string.lower()

if iterative_palindrome(clean_string):
	print("is a palindrome")
else:
	print("is not a palindrome")
