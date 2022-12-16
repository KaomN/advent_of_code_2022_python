fileInput = open('../input.txt', 'r')
lines = fileInput.readlines()

def countDis(str):
	s = set(str)
	return len(s)

for line in lines:
	for i in range(0, len(line)):
		if countDis(line[i:i+14]) == 14:
			marker = line[0:i+14]
			break
print(marker)
print(len(marker))