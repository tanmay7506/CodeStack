def count_positive_ignore_none(nums: list):
    '''
    Count the number of positive integers in the list, ignoring `None` values and zeros.

    Args:
        nums (list): A list of numbers, possibly containing `None` values.

    Returns:
        int: The count of positive integers in the list.
    '''
    count = 0
    for i in range(0,len(nums)):
        if nums[i] == None:
            continue
        elif type(nums[i]) == int:
           if nums[i] > 0:
                count += 1
    return count
