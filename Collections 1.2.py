# Reverse First half in an even length tuple
# Given an even-length tuple t, return a new tuple where the first half of the tuple is reversed, and the second half remains unchanged.


def reverse_first_half(t: tuple) -> tuple:
    '''
    Given an even-length tuple, return a new tuple where the first half 
    is reversed, and the second half remains unchanged.

    Arguments:
    t: tuple - an even-length tuple.

    Return: tuple - a new tuple with the first half reversed.
    '''
    l = list(t)
    return tuple(reversed(l[0:len(l)//2]))+tuple(l[len(l)//2:])
