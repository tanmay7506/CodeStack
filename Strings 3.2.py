# Most frequent first letter of a word in a multiline passage.
# Given a multi-line passage where the words are separated by spaces, find the letter which occurs most frequently as the first letter of any word. Consider both uppercase and lowercase letters as the same and return the letter in lowercase.

# Assume there will be only one letter that occurs the most number of times as the first letter of a word.


def most_occuring_first_letter(passage: str) -> str:
    '''
    Returns the letter which occurs most frequently 
    as the first letter of any word.(case insensitive)

    Args:
        passage (str): A multi-line string representing the passage.

    Returns:
        str: The most frequently occurring first letter in lowercase.
    '''
    words = passage.split()

    freq = {}

    for word in words:
        if word:  
            first_letter = word[0].lower() 
            freq[first_letter] = freq.get(first_letter, 0) + 1

    
    return max(freq, key=freq.get)
