print "Width: "
w = int(raw_input(""))

print "Length: "
l = int(raw_input(""))

def print_rect(l,w):
	for i in range(w):
		print ('*' * l)
print_rect(l,w)