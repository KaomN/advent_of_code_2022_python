fileInput = open('../input.txt', 'r')
lines = fileInput.readlines()

points = 0
count = 0
groups = 0;
for line in lines:
	if count == 2:
		groups += 1
		count = -1
	count += 1
commonChar = ["" for i in range(groups)]
priorities = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52}
count = 0
x = 0

for line in lines:
	if count == 0:
		one = line.strip()
		count = 1
	elif count == 1:
		two = line.strip()
		count = 2
	elif count == 2:
		three = line.strip()
		count = 0
		commonChar[x] = list(set(one)&set(two)&set(three))
		x += 1

for prio in commonChar:
 	points += priorities.get(prio[0])
print(points)