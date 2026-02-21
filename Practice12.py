n = int(input())

for i in range(n):        
    x, y = map(int, input().split(','))
    if i%2==0:
        print (x+y)
    if i%2!=0:
        print (abs(x-y))
