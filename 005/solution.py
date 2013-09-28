# Uses a nice trick; consider some x greater than 1 and less than or equal to 20, then:
# the smallest number divisible to x - 1 is a factor of the smallest number divisible to x.
# This allows us to expedite the process of calculation since we can increment the current
# value we're considering as a divisor by x - 1 each time we move to the next number 
# to check for being the smallest divisible from 1 to x.

def check_divisor(x, n):			
	for i in reversed(range(1, n + 1)):
		if x % i != 0:
			return False
	return True

def smallest_divisible_to(n):
	if n < 1:
		return False
	elif n == 1:
		return 1
	else:
		inc = smallest_divisible_to(n - 1)
		x = 0
		divisor_found = False
		while not divisor_found:
			x += inc
			divisor_found = check_divisor(x, n)
		return x

print smallest_divisible_to(20)