numList = (3, 5, 6, 4, 7, 8, 6)

#evensList = (x for x in numList if x % 2 == 0)

newList = ()
for x in numList:
	if x % 2 == 0:
		print x
	