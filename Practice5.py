n = int(input())
vowels = 'aeiouAEIOU'
for i in range(n):
    s = input()

    result = "".join(
        ch.upper() if ch in vowels else ch.lower()
        for ch in s
    )

    print(result)
