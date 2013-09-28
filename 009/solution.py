def triplet():
	for x in range(1, 500):
		for y in range(x, 500):
			for z in range(y, 500):
				if x**2 + y**2 == z**2 and x + y + z == 1000:
					return x * y * z

print triplet()