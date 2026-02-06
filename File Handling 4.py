'''
Write a function named num_to_words that accepts a square matrix of single digit numbers as argument. 
Within the function, create a file named words.csv. 
Write the matrix to the file by replacing the digits with their corresponding words. 
For example, num_to_words([[1, 2], [3, 4]]) should create the file words.csv with the following contents:

one,two
three,four
Note that the matrix will only have integers from 0 to 9, endpoints inclusive.
'''


def num_to_words(mat):
    """
    Convert matrix to file

    Argument: 
        mat: list of lists
    Return:
        None
    """
    digit_words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
    }
    
    with open("words.csv", "w") as f:
        for row in mat:
            words = [digit_words[num] for num in row]
            f.write(",".join(words) + "\n")   
