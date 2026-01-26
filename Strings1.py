# Format Elements in tuple as "second, first"
# Given a tuple of length two create a string in the format of "second, first" where first and second are the first and second elements in the tuple.

# The elements can be of any data type.


def format_as_second_comma_first(t: tuple) -> str:
    '''Formats the two elements in a tuple as "second, first".

    Arguments:
    t: tuple - a tuple two elements

    Return:
    str - a formatted string "second, first"

    Example:
    >>> format_as_second_comma_first(('hello', 'python'))
    'python, hello'
    >>> format_as_second_comma_first((1, 2))
    '2, 1'
    '''
    return f"{t[1]}, {t[0]}"
