def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """

    
    def inner(x): 
        while x > 10 ** k:
            if x % 10 != x // (10 ** k) % 10:
                return False
            x //= 10 ** k
        return True
    return inner
