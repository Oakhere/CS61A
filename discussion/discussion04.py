def even_weighted_loop(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_loop(x)
    [0, 6, 20]
    """
    new_list = []
    for i in range(len(s)):
        if i % 2 == 0:
            new_list += [s[i] * i]
    return new_list


# this is very important

def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if s == []:
        return 1
    else:
        with_first = s[0] * max_product(s[2:])
        without_first = max_product(s[1:])
        return max(with_first, without_first)
