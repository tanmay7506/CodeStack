n = int(input())
s = ''
for i in range(n):
    s += f"|{' '*i}\\{' '*(n-i-1)}|\n"
print(s)
