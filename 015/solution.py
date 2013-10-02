def num_routes(size):
	# Simply obtain the lower diagonal sequence and stick it in ways_to
	# At iteration x of the outer for-loop ways_to[x] = the number of ways 
	# to reach the diagonal x away from the top-left corner of the grid 
	ways_to = [1] * size
	for i in range(size):
		for j in range(i):
			ways_to[j] = ways_to[j] + ways_to[j-1]
		ways_to[i] = 2 * ways_to[i - 1]
		print ways_to
	return ways_to[size - 1]

print num_routes(20)