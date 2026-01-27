#Given an integer, check whether it is a palindrome. A palindrome is a number or a string that reads the same backward as forward.

def is_palindrome(n: int) -> bool:
    '''Checks if an integer is a palindrome.

    Arguments:
    n: int - the integer to check

    Return:
    bool - True if the integer is a palindrome, False otherwise
    '''
    rev_n = str(n)[::-1]
    return (str(n) == rev_n)
