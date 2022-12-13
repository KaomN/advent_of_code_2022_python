fileInput = open('../input.txt', 'r')
lines = fileInput.readlines()
count = 0
# Get length for list
for line in lines:
	if line.strip() == "":
		count += 1
count += 1
calorieArray = [0 for i in range(count)]
calories = 0
count = 0

for line in lines:
	if line.strip() == "":
		calorieArray[count] = calories
		count += 1
		calories = 0
	else:
		calories += int(line.strip())
calorieArray[count] = calories

calorieArray.sort(reverse=True)
print(calorieArray[0]+calorieArray[1]+calorieArray[2])