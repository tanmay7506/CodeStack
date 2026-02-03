# filename is a text file that contains a collection of words in lower case, one word on each line. 
# Write a function named get_freq that accepts filename as argument. 
# It should return a dictionary where the keys are distinct words in the file, the values are the frequencies of these words in the file.


def get_freq(filename):
    """
    Extract frequency information from the file

    Argument:
        filename: string, path to file
    Return:
        result: dictionary; keys are strings, values are integers
    """
    
    freq = {}
    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            if word:                     # ignore empty lines if any
                freq[word] = freq.get(word, 0) + 1
    return freq
