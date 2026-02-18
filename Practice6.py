def get_filter_func(criteria, data):
    if criteria is None:
        return lambda x: True
    if criteria == 'fail':
        return lambda x: x<40
    if criteria == 'toppers':
        return lambda x: x>=90

    marks = [row[1] for row in data]
    avg = sum(marks)/len(marks)
    if criteria == 'above_average':
        return lambda x:x>=avg
    if criteria == 'below_average':
        return lambda x:x<avg

def get_roll_nos(data:list, criteria=None):
    '''
    Filter roll numbers based on criteria.

    Args:
        data (list): List of tuples with roll number and marks.
        criteria (str, optional): The criteria for filtering.

    Returns:
        list: List of roll numbers matching the criteria or None if invalid criteria.
    '''
    
    
    filter_func = get_filter_func(criteria, data)
    if filter_func is not None:
        return [rollno for rollno, marks in data if filter_func(marks)]
    
