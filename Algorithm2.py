
fibList = [1, 2]
sumList = 2

for i in range (2, 4000000):
    x = fibList[i-1] + fibList[i-2]
    fibList.insert(i, x)

    if x > 4000001:
    	break

    if (x%2 == 0):
    	sumList += x
#print fibList
print sumList