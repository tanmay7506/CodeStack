def average(marks):
    return sum(marks)/len(marks)

def filter_students(data: dict, criteria: str) -> set:
    
    if criteria == 'excellent':
        return {
            name for name, marks in data.items() 
            if average(marks) >= 85
        }
    elif criteria == 'good':
        return {
            name for name, marks in data.items() 
            if 50 <= average(marks) < 85
        }
    elif criteria == 'all_pass':
        return {
            name for name, marks in data.items() 
            if all(map(lambda x: x >= 50, marks))
        }
    elif criteria == 'balanced':
        return {
            name for name, marks in data.items() 
            if max(marks)-min(marks) <= 10
        }
