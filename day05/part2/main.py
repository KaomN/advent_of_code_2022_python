fileInput = open('../input.txt', 'r')
lines = fileInput.readlines()

stack = [
	["B", "V", "S", "N", "T", "C", "H", "Q"],
	["W", "D", "B", "G"],
	["F", "W", "R", "T", "S", "Q", "B"],
	["L", "G", "W", "S", "Z", "J", "D", "N"],
	["M", "P", "D", "V", "F"],
	["F", "W", "J"],
	["L", "N", "Q", "B", "J", "V"],
	["G", "T", "R", "C", "J", "Q", "S", "N"],
	["J", "S", "Q", "C", "W", "D", "M"]
]

# stack = [
# 	["Z", "N"],
# 	["M", "C", "D"],
# 	["P"]
# ]


moveFrom = 0
moveTo = 0
quantity = 0
answer = ""


for line in lines:
	num = [int(s) for s in line.split() if s.isdigit()]
	quantity = num[0]
	moveFrom = num[1] - 1
	moveTo = num[2] - 1
	if quantity > 1:
		tempList = [""] * 40
		
		for x in range(quantity):
			tempList[x] = stack[moveFrom].pop(len(stack[moveFrom]) - 1)
		for x in range(quantity, 0, -1):
			stack[moveTo].append(tempList[x - 1])
	else:
		stack[moveTo].append(stack[moveFrom].pop(len(stack[moveFrom]) - 1))
	print(stack)


for x in range(len(stack)):
	answer += stack[x][len(stack[x]) - 1]
print(answer)