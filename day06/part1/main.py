fileInput = open('../input.txt', 'r')
lines = fileInput.readlines()

def countDis(str):
	s = set(str)
	return len(s)

for line in lines:
	for i in range(0, len(line)):
		if countDis(line[i:i+4]) == 4:
			marker = line[0:i+4]
			break
print(len(marker))