n = int(input())
s = ''
for i in range(n):
    s += f"|{' '*(n-i-1)}/{' '*(2*i)}\\{' '*(n-i-1)}|\n"
print(s)
