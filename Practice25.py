n = int(input())
names = []

for _ in range(n):
    name = input()
    parts = name.split()
    short_name = f'{". ".join(map(lambda x: x[0], parts[:-1]))}. {parts[-1]}'
    names.append(short_name)

for name in sorted(names):
    print(name)
