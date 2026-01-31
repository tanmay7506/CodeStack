# Check if an even-length string has A or a in the second half
# Given an even-length string s, check if the second half contains the character "a" or "A". Return True if it does, otherwise return False.

def has_a_in_second_half(s: str) -> bool:
    '''
    Given an even-length string, check if the second half contains 
    the character "a" or "A".

    Arguments:
    s: str - an even-length string.

    Return: bool - True if "a" or "A" is found in the second half, else False.
    '''
    l = list(s)
    for i in range(len(s)//2,len(s)):
        if l[i] == 'a' or l[i] == 'A':
            return True
    return False
