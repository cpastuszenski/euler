import math

def lpf(n):
	if n < 1:
		raise ValueError('lpf() doesn\'t handle numbers < 1.')
	factors = []
	# handle evens
	while n % 2 == 0:
		factors.append(2)
		n //= 2
	# handle odds; we only need to go up to sqrt(n), however
	bound = math.sqrt(n + 1)
	i = 3
	while i <= bound:
		if n % i == 0:
			factors.append(i)
			n //= i
			bound = math.sqrt(n + i)
		else:
			i += 2
	if n != 1:
		factors.append(n)
	return factors

print max(lpf(600851475143))