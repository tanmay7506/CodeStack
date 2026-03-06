vowel_count = 0
consonant_count = 0
for c in s[::2].lower():
  if c in "aeiou":
    vowel_count += 1
  elif c.isalpha():
     consonant_count += 1
print(vowel_count, consonant_count)  
