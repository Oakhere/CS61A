def prime_factors(n):
	"""Print the prime factor of n in non-decreasing order.

	>>> prime_factors(8)
	2
	2
	2
	>>> prime_factors(9)
	3
	3
	>>> prime_factors(10)
	2
	5
	>>> prime_factors(11)
	11
	>>> prime_factors(12)
	2
	2
	3
	>>> prime_factors(858)
	2
	3
	11
	13
	"""

	while n > 1:
		k = smallest_factor(n)
		n = n // k
		print(k)

def smallest_factor(n):
	k = 2
	while k <= n:
		if n % k == 0:
			return k
		k += 1
	