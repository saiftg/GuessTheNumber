myList1 = [1,2,3,5,7]
myList2 = [6,7,8,2]

if len(myList1) == len(myList2):

	sums =[myList1[i] + myList2[i] for i in range(len(myList1))]

	print sums

else:
	print"List length not compatible"
