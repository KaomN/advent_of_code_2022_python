fileInput = open('../input.txt', 'r')
lines = fileInput.readlines()

count = 0
mostCalories = 0;
calories = 0;
for line in lines:
	count += 1
	if line.strip() == "":
		if mostCalories < calories:
			mostCalories = calories
		calories = 0
	else:
		calories += int(line.strip())
print(mostCalories)