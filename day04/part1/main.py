fileInput = open('../input.txt', 'r')
lines = fileInput.readlines()

def checkIfContained(line):
	section = line.strip().split(',')
	pairOne = section[0].split('-')
	pairTwo = section[1].split('-')
	pairOneLen = abs(int(pairOne[0]) - int(pairOne[1]))
	pairTwoLen = abs(int(pairTwo[0]) - int(pairTwo[1]))
	pairOneLen += 1
	pairTwoLen += 1
	if pairOneLen < pairTwoLen:
		if int(pairOne[0]) >= int(pairTwo[0]) and int(pairOne[1]) <= int(pairTwo[1]):
			return 1
		else:
			return 0
	elif pairOneLen == pairTwoLen:
		if int(pairOne[0]) == int(pairTwo[0]) and int(pairOne[1]) == int(pairTwo[1]):
			return 1
		else:
			return 0
	elif pairOneLen > pairTwoLen:
		if int(pairOne[0]) <= int(pairTwo[0]) and int(pairOne[1]) >= int(pairTwo[1]):
			return 1
		else:
			return 0

count = 0

for line in lines:
	count += checkIfContained(line)
print(count)
