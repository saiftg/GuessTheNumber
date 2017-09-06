
import random
secret_number = random.randint(1,10)
print secret_number

print "I am thinking of a number between 1 and 10"

#for turns in range(1,6):
#print "Pick a number:"


#numberGuessed = int(number)
#if numberGuessed == secret_number:
#	print "Correct!"
keep_guessing = True
total_turns = 5
used_turns = 0;

while keep_guessing == True:
	numberGuessed = int(raw_input("Pick a number:\n"))
	#numberGuessed = random.randint(1,10)
	used_turns += 1
	if (numberGuessed == secret_number):
		print "Yes! You guessed it " 
		keep_guessing = False
	elif (total_turns == used_turns):
		print "Outta turns!"
		keep_guessing = False
	else:
		if(numberGuessed < secret_number):
			print "Too Low"
		else:
			print "Nope."
	