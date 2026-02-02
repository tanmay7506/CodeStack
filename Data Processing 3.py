# Find largest sub sequence with the antakshari property
# The input is in multiple lines. The first line contains a positive integer n. This is followed by n lines, each containing sequences of words. Each line thus consists of multiple words, separated by commas, with no spaces in between words.

# You have to output, for each line, the length of the longest subsequence of words following the antakshari property.

# Assume all words are lowercase.

# A sub-sequence is a subset of consecutive words in this sequence.

# A sub-sequence is said to have the antakshari property if the last letter of every word is equal to the first letter in the next word in the sequence.


n = int(input())

for _ in range(n):
    words = input().strip().split(',')
    
    max_len = 1
    curr_len = 1
    
    for i in range(len(words) - 1):
        if words[i][-1] == words[i+1][0]:
            curr_len += 1
        else:
            curr_len = 1
        max_len = max(max_len, curr_len)
    
    print(max_len)
