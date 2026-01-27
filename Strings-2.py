def even_first_odd_reversed(s: str) -> str:
    '''Return a string with the characters in the even indices first 
    and the characters in the odd indices reversed next.

    Arguments:
    s: str - the input string

    Return:
    str - modified string

    Example:
    >>> even_first_odd_reversed('abcde')
    'acedb'
    >>> even_first_odd_reversed('python')
    'ptonhy'
    '''
    even_chars = s[0::2]
    odd_chars = s[1::2]
    rev_odd_chars = odd_chars[::-1]
    return (even_chars+rev_odd_chars)
