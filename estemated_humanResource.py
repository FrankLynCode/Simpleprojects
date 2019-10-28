import math

standar_Size = 80
size = 0
timeOrPeople = 0
def estemated(type=1,size=1,timeOrPeople=0):
    if type == 1 and timeOrPeople != 0:
        return math.ceil(size*standar_Size/timeOrPeople)

    if type == 2 and timeOrPeople != 0:
    	return size*standar_Size/timeOrPeople

while True:
	type = int(input("Input 1 for estemate people, 2 for estemate time:"))
	if type == 1 or type == 2:
		break
	print("Only 1 or 2 available")
if type == 1:
	size = int(input("Input work size:"))
	timeOrPeople=int(input("Input expected time:"))
else:
	size = int(input("Input work size:"))
	timeOrPeople=int(input("Input working People:"))

print(estemated(type,size,timeOrPeople))