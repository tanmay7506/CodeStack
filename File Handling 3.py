filename is a CSV file that has the following header:

Name,Country,Goals
The first five lines of a sample file are given below:

Name,Country,Goals                                        
P1,Brazil,20  
P2,Argentina,30
P3,Brazil,50                                                   
P4,Germany,30
Write a function named get_goals that accepts filename and the name of a country as arguments. 
It should return a tuple having two elements: (num_players, num_goals). 
num_players is the number of players from this country that appear in this file, num_goals is the total number of goals scored by all the players who belong to this country. 
If the country is not present in the file, then return the tuple (-1, -1).

def get_goals(filename, country):
    """
    Get the count of players and their cumulative goals for this country

    Arguments:
        filename: string
        country: string
    Return: 
        result: tuple, (integer, integer)
    """
    with open(filename, 'r') as f:
        f.readline()  # skip header
        
        num_players = 0
        num_goals = 0
        
        for line in f:
            name, ctry, goals = line.strip().split(',')
            if ctry == country:
                num_players += 1
                num_goals += int(goals)
    
    if num_players == 0:
        return (-1, -1)
    
    return (num_players, num_goals)
    
