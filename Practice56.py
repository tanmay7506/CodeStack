n = int(input())
for i in range(1,n+1):
    zeros = " ".join("0"*i)
    print(" "*(n-i)+zeros)
