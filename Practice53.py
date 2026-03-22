 vowels = "aeiouAEIOU"
    result = []
    for char in s:
        if char in vowels:
            result.append(chr(ord(char) + 1))
        else:
            result.append(char)
    print(''.join(result))
