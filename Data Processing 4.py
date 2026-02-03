# Hyphen seperated word digits of a number
# Given an integer, generate a string with its digits as words separated by hyphens


def num_to_word(num: int) -> str:
    '''
    Given an integer, generate a string with its digits as words separated by hyphens.

    Arguments:
    num: int - the input number

    Return:
    str - the string with digits as words separated by hyphens
    '''
    words = ["zero", "one", "two", "three", "four", 
             "five", "six", "seven", "eight", "nine"]
    
    result = "-".join(words[int(d)] for d in str(num))
    return result
