
print"Enter a word:"
word = raw_input("")

newWord = word

vowelsList = ('oo', 'ee', 'ii', 'aa', 'uu')

for x in word.lower():
	if x in vowelsList:
		newWord = newWord.replace(x,'pp')

print newWord


