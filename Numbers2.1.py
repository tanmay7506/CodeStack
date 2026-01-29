# Given an integer seconds, return a tuple (minutes, remaining_seconds) where minutes is the number of full minutes in seconds, and remaining_seconds is the leftover seconds.

def seconds_to_minute_seconds(seconds: int) -> tuple:
    '''
    Given an integer representing seconds, return a tuple of (minutes, seconds).

    Arguments:
    seconds: int - an integer representing the number of seconds.

    Return: tuple - a tuple of (minutes, remaining_seconds).
    '''
    minutes = seconds//60
    remaining_seconds = seconds%60
    return (minutes, remaining_seconds)
