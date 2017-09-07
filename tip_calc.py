print "Total Bill amount?: "
bill = float(raw_input(""))

print "Was service good, fair or bad?"
feedback = raw_input("")

service = feedback.upper()

print service

if service == "GOOD":
	print "Total bill is " + "${:.2f}".format(bill * 1.20)
elif service == "FAIR":
	print "Total bill is " + "${:.2f}".format(bill * 1.15)
elif service == "BAD":
	print "Total bill is " + "${:.2f}".format(bill * 1.10)

