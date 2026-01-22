# find_min: Find the minimum value in a list of integers.
  # Input: A list of integers.
  # Output: An integer, the minimum value in the list.
# odd_increment_even_decrement_no_modify: Increment all the odd numbers in a list by 1 and decrement all the even numbers by 1, without modifying the original list.
  # Input: A list of integers.
  # Output: A new list of integers with the modified values.
# odd_square_even_double_modify: Square all the odd numbers and double all the even numbers in a list, modifying the list in place.
  # Input: A list of integers.
  # Output: None (the input list is modified in place).
# more_than_two_unique_vowels: Given a string of comma-separated words, return a set containing words that have more than two unique vowels.
  # Input: A string of comma-separated words.
  # Output: A set of words with more than two unique vowels.
# sum_of_list_of_lists: Given a list of lists of integers, find the sum of all the integers in all the lists.
  # Input: A list of lists of integers.
  # Output: An integer, the sum of all the integers in the nested lists.
# flatten: Flatten a list of lists into a single list.
  # Input: A list of lists.
  # Output: A single flattened list.
# all_common: Find the common characters that are present in all strings in a list of strings and return them as a string in ascending order.
  # Input: A list of strings.
  # Output: A string containing common characters in ascending order.
# vocabulary: Given a list of sentences (with only alphabets and spaces), find the vocabulary (list of unique words) and return it as a set. Convert all words to lowercase before adding to the vocabulary.
  # Input: A list of sentences.
  # Output: A set of unique words in lowercase.


min =  None

def find_min(items:list):
    min = items[0]
    for item in items[1:]:
        if item<min:
            min = item
    return min


def odd_increment_even_decrement_no_modify(items) -> list:
    items_copy = []
    for num in items:
        if num%2!=0:
            num = num+1
            items_copy.append(num)
        else:
            num = num-1
            items_copy.append(num)
    return items_copy


def odd_square_even_double_modify(items:list) -> list:
    for i in range(len(items)):
        if items[i]%2!=0:
            items[i]**=2
        else:
            items[i]*=2


def more_than_two_unique_vowels(sentence):
    vowels = set("aeiou")
    words = set()
    for word in sentence.split(","):
        if len(set(word) & vowels)>2:
            words.add(word)
    return words
    

def sum_of_list_of_lists(lol):
    sum = 0
    for i in lol:
        for n in i:
            sum+= n
    return sum


def flatten(lol):
    flat = []
    for row in lol:
        for item in row:
            flat.append(item)
    return flat


def all_common(strings):
    common_char = set(strings[0])
    for string in strings[1:]:
        common_char &= set(string)
    return ''.join(sorted(common_char))


def vocabulary(sentences):
    vocab = set()
    for sentence in sentences:
        for word in sentence.split(" "):
            vocab.add(word.lower())
    return vocab
