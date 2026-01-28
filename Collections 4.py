# Given a string, return a set of unique vowels present in the string.

def unique_vowels(s: str) -> set:
    '''
    Given a string, return a set of unique vowels present in the string.

    Arguments:
    s: str - the input string

    Return:
    set - a set of unique vowels present in the string

    Examples:
    >>> unique_vowels('banana treat')
    {'a', 'e'}
    >>> unique_vowels('apple lolipop')
    {'a', 'e', 'i', 'o'}
    >>> unique_vowels('Ian Avinkov')
    {'I','A','a','i','o'}
    '''
    s1 = set(s)
    l1 = set('aeiouAEIOU')
    return s1&l1
