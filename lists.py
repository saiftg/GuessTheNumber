


students = ["Huey", "Dewey", "Stewie", "Launchpad"]


print students
print students[0]
print students[-1]


atlanta_teams = ["Falcons", "Thrashers", "Hawks", "Braves"]
print atlanta_teams

#atlanta_teams.pop()
#print atlanta_teams

atlanta_teams.append("Atl Utd")
print atlanta_teams

atlanta_teams_length = len(atlanta_teams)
for i in range(0,(atlanta_teams_length-1)):
	
	if(atlanta_teams[i]) == "Thrashers":
		atlanta_teams.pop(i)
print atlanta_teams


teams_string = "Falcons, Braves, Hawks, Atl Utd"
print teams_string
teams_list = teams_string.split(" ,")
print teams_list

#print atlanta_teams



baseball_basketball = atlanta_teams[2:3]
print	baseball_basketball