def last_word_starts_with_upper_case(sentence: str):
    """
    Find the last word in a sentence that starts with an uppercase letter.

    Args:
        sentence (str): The input sentence.

    Returns:
        str or None: The last word starting with an uppercase letter, or None if no such word exists.
    """
    
    
    last_word = None
    for word in sentence.split():
        if word[0].isupper():
            last_word = word
    return last_word
