from collections import defaultdict
import math

# Solution uses the fact (see http://www.math.mtu.edu/mathlab/COURSES/holt/dnt/divis2.html)
# that the number of divisors of a number is equal to the product of the exponents
# of the terms in the number's prime factorialization, with one added to each of them

_triangle_dict = {1 : 1} # start with the first tri number
def populate_triangles(n):
	if n < 1:
		return 0
	try:
		return _triangle_dict[n]
	except KeyError:
		tri = n + populate_triangles(n - 1)
		_triangle_dict[n] = tri
		return tri

def prime_factorize(n):
	if n < 1:
		raise ValueError('prime_factorize() expects numbers >= 1.')
	if n == 0:
		return []
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

def triangle_divisors(n):
	factors = prime_factorize(n)
	distribution = defaultdict(int)
	for x in factors:
		distribution[x] += 1
	try:
		return reduce(lambda x, y: x * y, [exp + 1 for exp in distribution.values()])
	except:
		return 1

triangle_list = (populate_triangles(n) for n in range(1, 1000000))
highly_disvisible_tri = (tri for tri in triangle_list if triangle_divisors(tri) > 500)
print highly_disvisible_tri.next()