def is_odd_length_palindrome(s: str) -> bool:
    '''Check if a string is a palindrome with odd length.

    Args:
        s : str - input string

    Returns:
        bool - True if s is a palindrome with odd length, False otherwise.
    '''
    rev_s = s[::-1]
    if len(s)%2==0:
        return False
    elif len(s)%2!=0:
        if s == rev_s:
            return True
        else:
            return False
