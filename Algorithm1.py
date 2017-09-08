

threesList = []
fivesList = []
fifteensList = []

i = 1

for i in range(1,1000):
	if (i%3 == 0):
		threesList.append(i)

for i in range(1,1000):
	if (i%5 == 0):
		fivesList.append(i)

for i in range(1,1000):
	if (i%15 == 0):
		fifteensList.append(i)


sumList = (sum(threesList) + sum(fivesList)) - sum(fifteensList)
	
print sumList
