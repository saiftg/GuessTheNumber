


classSize = 19;
question = "How big is class?";
print question
response = raw_input(">")

response_as_an_int = int(response)
if (response_as_an_int != classSize):
	print "You are from a different class"
else:
	print "Lets code!"

import random;
rand_number = random.randint(1,10)
print rand_number

keep_going = True
while keep_going:
	get_answer = raw_input("Hit any key")
	keep_going = False
print "Which one is the Any key?"