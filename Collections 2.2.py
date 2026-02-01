# Delete the first three elements in a list
# Given a list l, modify it in place by deleting the first three elements. If the list has fewer than three elements, delete all elements.


def delete_first_three(l: list) -> None:
    '''
    Given a list, delete the first three elements in the list.

    Arguments:
    l: list - a list of elements.

    Return: None - the list is modified in place.
    '''
    if len(l)<3:
        del l[0:]
        return l
    else:
        del l[0], l[0], l[0]
        return l
