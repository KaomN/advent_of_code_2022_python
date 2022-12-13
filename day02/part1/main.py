'''
			  Points
Lose			0
Draw			3
Win				6
Opponent
A = Rock
B = Paper
C = Scissors
You
X = Rock		1
Y = Paper		2
Z = Scissors	3
'''
fileInput = open('../input.txt', 'r')
lines = fileInput.readlines()
points = 0
for line in lines:
	if line.strip() == "A Y":
		points += 8
	elif line.strip() == "A X":
		points += 4
	elif line.strip() == "A Z":
		points += 3
	elif line.strip() == "B X":
		points += 1
	elif line.strip() == "B Y":
		points += 5
	elif line.strip() == "B Z":
		points += 9
	elif line.strip() == "C X":
		points += 7
	elif line.strip() == "C Y":
		points += 2
	elif line.strip() == "C Z":
		points += 6
print(points)