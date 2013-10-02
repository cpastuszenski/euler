def next(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1

_cache = {}
def collatz_len(n):
	if n < 1:
		raise ValueError("Cannot perform a Collatz sequence starting with a number lower than 1")
	elif n == 1:
		return 1

	len = 1
	curr = n

	while 1:
		curr = next(curr)
		try:
			len += _cache[curr]
			break
		except:
			len += 1
			if curr == 1:
				break
	_cache[n] = len
	return len

max_len = 0
max_num = None
for i in range(1, 1000000):
	len = collatz_len(i)
	if len > max_len:
		max_len = len
		max_num = i
print max_num

