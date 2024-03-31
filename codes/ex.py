"""Our first Python source file"""

from operator import floordiv, mod

def divide_exact(n,d=10):
	"""Return the quotient and remainder of dividing N by D.
    
    >>> q, r = divide_exact(2023, 10)
    >>> q
    202
    >>> r
    3
	"""
	return floordiv(n,d), mod(n,d)



