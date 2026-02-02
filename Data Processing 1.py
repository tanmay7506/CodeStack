# Find the index of the row with maximum number of zeros in a matrix
# Given a m x n matrix, find the index of the row with the maximum number of zeros. Assume there will be only one row with the maximum number of zeros.


def row_index_with_most_number_of_zeros(matrix:list)->int:
    '''
    Arguments: matrix: list[list] 
    Rertun: int - index of the row with the maximum number of zeros.
    '''
    max_zeros = -1
    row_index = -1
    
    for i in range(len(matrix)):
        count = matrix[i].count(0)
        if count > max_zeros:
            max_zeros = count
            row_index = i
    
    return row_index
