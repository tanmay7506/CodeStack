n = int(input().strip())

if n == 1:
    print("v")
else:
    for i in range(n - 1):      #constructs line char by char            
        left_spaces = " " * i   #makes left spaces as per line requirement
        inner_spaces = " " * (2 * (n - i - 1) - 1)  #make inner spaces as per line requirement
        
        line = left_spaces + "\\" + inner_spaces + "/"  #puts things together
        print(line)
    
    print(" " * (n - 1) + "v")
