def vowel_count(word):
    return sum(1 for char in word if char.lower() in "aeiou")

words = input().split()
print(" ".join([f"{word}({vowel_count(word)})" for word in words]))
