a,b = str(num)[-2:]
a, b = int(a), int(b)
return a!=0 and b!=0 and num % a == 0 and num % b == 0
