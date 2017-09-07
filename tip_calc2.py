print "Total Bill amount?: "
bill = float(raw_input(""))

print "How many peeps?: "
peeps = int(raw_input(""))

print "Was service good, fair or bad?"
feedback = raw_input("")

service = feedback.upper()

tip1 = bill * 0.20
tip2 = bill * 0.15
tip3 = bill * 0.10

split1 = (bill + tip1)/peeps
split2 = (bill + tip2)/peeps
split3 = (bill + tip3)/peeps

if service == "GOOD":
	print "Total bill is " + "${:.2f}".format(bill * 1.20) 
	print "The tip was $" + str(tip1)
	print "Amounr per person: $" + str(split1)

elif service == "FAIR":
	print "Total bill is " + "${:.2f}".format(bill * 1.15) 
	print "The tip was $" + str(tip2)
	print "Amounr per person: $" + str(split2)

elif service == "BAD":
	print "Total bill is " + "${:.2f}".format(bill * 1.10) 
	print "The tip was $" + str(tip3)
	print "Amounr per person: $" + str(split3)


