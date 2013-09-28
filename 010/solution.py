import itertools

# Using Sieve of Eratosthenes
def sieve():
	M = {} # map between composite integer and the first-found prime factor
	q = 2
	while 1:
		if q not in M:
			yield q # q is a prime, so yield it
			M[q**2] = [q] # q^2 definitely isn't a prime, though, so mark it as composite
		else:
			for p in M[q]: # move prime to next multiple
				M.setdefault(p + q, []).append(p) # set up the dict entry if empty; add prime in any case
		q += 1

print sum(takewhile(lambda n: n < 2000000, sieve()))