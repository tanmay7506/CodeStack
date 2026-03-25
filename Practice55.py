def process_sentence(sentence: str, task: str):
    
    words = sentence.split()
    if task == 'count_words':
        return len(words)
    elif task == 'count_palindromes':
        return sum(1 for word in words if word == word[::-1])
    elif task == 'count_words_with_repeated_chars':
        return sum(1 for word in words if len(word) != len(set(word)))
    elif task == 'words_with_max_len':
        max_len = max(map(len, words))
        max_len_words = {word for word in words if len(word) == max_len}
        return max_len_words
