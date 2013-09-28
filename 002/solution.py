sum, x, y = 0, 1, 2
while y < 4000000:
	if y % 2 == 0:
		sum += y
	x, y = y, x + y
print sum