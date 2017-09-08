

myList = [2,4,5,7,3,7,2]
print myList

print"Enter a multiplier: "
num = int(raw_input(""))

newList = []
for i in myList:
	newList.append(i * num)

	print newList