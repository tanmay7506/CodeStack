'''
Write a function named relation that accepts these two text files as arguments. 
It should return the string Subset if file1 is a subset of file2. 
It should return Equal if file1 is equal to file2.
If both these conditions are not satisfied, it should return the string No Relation.
'''

def relation(file1, file2):
    """
    Determine the relationship between two files

    Arguments:
        file1, file2: strings, paths to two files
    Return:
        string: 'Equal', 'Subset' or 'No Relation'
    """
    with open(file1, 'r') as f1:
        lines1 = [line.strip() for line in f1.readlines()]
    with open(file2, 'r') as f2:
        lines2 = [line.strip() for line in f2.readlines()]

    f1_len = len(lines1)
    f2_len = len(lines2)

    same_prefix = (lines1 == lines2[:f1_len])

    if same_prefix and f1_len == f2_len:
        return "Equal"

    if same_prefix and f1_len < f2_len:
        return "Subset"

    return "No Relation"
