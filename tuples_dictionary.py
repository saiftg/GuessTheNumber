

a_tuple = (1,2,3) #tuples are unchangeable and in parentheses


# Dictionaries are just like lists but they have english indices 

zombie = {}
zombie["weapon"] = "Axe" 
zombie["health"] = "100"

print zombie

for key, value in zombie.items():
	print"Zombie has %s with %s" % (key, value)
	print"ZOmbie %s with %s" % (key, zombie[key])

zombies = []
zombies.append({
	"speed": 13
	"weapon": "Gun"
	"Name" : "Jim"
	})
zombies.append({
	"speed" : 14
	"weapon" : "Bat"
	"Name" : "Frank"
	"Victims" : [
		"jane"
		"tina"
		"stephan"
		]
	})
print zombies[1]["victims"][1]