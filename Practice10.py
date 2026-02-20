def replace_middle_with_n_times_middle(t: tuple, n: int) -> tuple:
    '''
    Replace the middle element of a tuple with `n` copies of the middle element.

    Args:
        t (tuple): A tuple with an odd number of elements.
        n (int): The number of times the middle element should be repeated.

    Returns:
        tuple: A new tuple with the middle element replaced by `n` copies.
    '''
    l=[]
    for i in t:
        l += [i]
    for j in range(n-1):
        k = len(l)//2
        l.insert(k, l[k])
    t1 = tuple(l.copy())
    return t1
