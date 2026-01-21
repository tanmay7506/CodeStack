# Write a program to solve these tasks. Use loops where necessary.
# Tasks:
# factors - Find the factors of a number n (including 1 and itself) in ascending order.
# find_min - Take n numbers from the input and print the minimum number.
# prime_check - Check whether a given number is prime or not.
# is_sorted - Check if all characters of the given string from input are in alphabetical order. Print the output as "True" or "False" accordingly.
# any_true - Take n numbers from input and check if any of the numbers are divisible by 3. Print the output as "True" or "False" accordingly.
# manhattan - Take inputs directions such as "UP", "DOWN", "LEFT" and "RIGHT" from the input until the input is "STOP". Assume you are starting from (0,0) in a cartesian coordinate. Find the Manhattan distance between the starting point and the ending point by following the steps in the cartesian plane.


task = input()

if task == "factors":
    num = int(input())
    factors = 1
    for i in range(1,num+1):
        if (num%i == 0):
            print(i)


elif task == "find_min":
    n = int(input())
    min= 100000

    for i in range(n):
        num = int(input())
        if num < min:
            min = num

    print(min)

    

elif task == "prime_check":
    num = int(input())
    flag = "False"
    if num <= 1:
        print("False")
    else:
        for i in range(2, int(num**0.5) + 1):  # check till square root of num
            if num % i == 0:
                flag = "False"
                break
            else:
                flag = "True"
    print(flag)
    

elif task == "is_sorted":
    string = input()
    if list(string) == sorted(string):
        print("True")
    else:
        print("False")
    

elif task == "any_true":
    n = int(input())
    nums = []

    for i in range(n):
        num = int(input())
        nums.append(num)

    found = False
    for num in nums:
        if num % 3 == 0:
            found = True
            break
    
    print(found)


elif task == "manhattan":
    
    x, y = 0, 0  # starting coordinates

    while True:
        direction = input().strip().upper()  # take direction, case-insensitive

        if direction == "STOP":
            break
        elif direction == "UP":
            y += 1
        elif direction == "DOWN":
            y -= 1
        elif direction == "LEFT":
            x -= 1
        elif direction == "RIGHT":
            x += 1
        else:
            print("Invalid direction!")


    distance = abs(x) + abs(y)
    print(distance)
