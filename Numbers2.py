# Write a function to check if a number is a ten-digit even number.
# Also account for negative numbers discarding the sign.


def is_ten_digit_even(n):
    '''Checks if a number is a 10 digit even number.

    Also account for negative numbers discarding the sign.

    Args: 
        n (int): The given number. 
    
    Returns: 
        bool : result as True or False. 
    
    Examples:
    >>> is_ten_digit_even(8769473839)
    False
    >>> is_ten_digit_even(928948)
    False
    >>> is_ten_digit_even(9289479278)
    True
    >>> is_ten_digit_even(-9289479278)
    True
    '''
    if n >= 0:
        if n%2==0 and len(str(n))==10:
            return True
        else:
            return False
    else:
        if n%2==0 and len(str(n)[1:])==10:
            return True
        else:
            return False
