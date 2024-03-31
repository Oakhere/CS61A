def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    k = 0
    m = 0
    while k < 10:
        if has_digit(n, k):
            m += 1
        k += 1
    return m

def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    while n != 0:
        r = n % 10
        if r == k:
            return True
        else:
            n //= 10
    return False

