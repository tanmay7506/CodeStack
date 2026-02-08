'''
P is a dictionary of father-son relationships that has the following structure: for any key in the dictionary, its corresponding value is the father of key. As an example:

P = {
    'Jahangir': 'Akbar', 
    'Akbar': 'Humayun', 
    'Humayun': 'Babur'    
}

If 'Jahangir' is the key, then 'Akbar', his father, is the value. This is true of every key in the dictionary.

Write a recursive function named ancestry that accepts the following arguments:

P: dictionary of relationships
present: name of a person, string
past: name of a person, string
It should return the sequence of ancestors of the person named present, traced all the way back up to person named past. For example, ancestry(P, 'Jahangir', 'Babur') should return the list:

L = ['Jahangir', 'Akbar', 'Humayun', 'Babur']

In more Pythonic terms, L[i] is the father of L[i - 1], for 1≤i<len(L), with the condition that L[0] should be present and L[-1] should be past.
'''

def ancestry(P, present, past):
    """
    A recursive function to compute the sequence of ancestors of person

    Arguments:
        P: dict, key and value are strings
        present: string
        past: string
    Return:
        result: list of strings
    """
    if present == past:
        return [present]
    
    return [present] + ancestry(P, P[present], past)
