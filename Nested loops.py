#Tasks
#Permutation (permutation): Given a string s, print all the possible two-letter permutations(without repitition) of the letters in the string.

#Sorted Permutation (sorted_permutation): Given a string s, print all the possible two-letter permutations(without repetition) of the letters in the string where the first character comes before the second one in alphabetical order. The order in which the permutations are printed is same as the previous one (Type: Filtering).

#Repeat the Repeat (repeat_the_repeat): Given a number n, print the numbers from 1 to n in the same line and repeat this n times.

#Repeat Incrementally (repeat_incrementally): Given a number n, print a pattern where the k-th line contains the first k numbers and there are n lines in total. For example, if n is 4, the output should be:
'''
1
12
123
1234
'''

#Increment and Decrement (increment_and_decrement): Given a number n, print a pattern where the k-th line should have the numbers from 1 to k and then back down to 1. For example, if n is 4, the output should be:
'''
1
121
12321
1234321
'''

task = input()

if task == "permutation":
    s = input().strip()
    n = len(s)
    result = []
    for i in range(n):
        for j in range(n):
            if i != j:  # avoid repetition
                result.append(s[i] + s[j])
    print("\n".join(result))


elif task == "sorted_permutation":
    s = input().strip()
    n = len(s)
    result = []
    for i in range(n):
        for j in range(n):
            if i != j and s[i] < s[j]:  # first < second alphabetically
                result.append(s[i] + s[j])
    print("\n".join(result))


elif task == "repeat_the_repeat":
    n = int(input())
    line = "".join(str(i) for i in range(1, n+1))
    for _ in range(n):
        print(line)


elif task == "repeat_incrementally":
    n = int(input())
    for k in range(1, n+1):
        line = "".join(str(i) for i in range(1, k+1))
        print(line)


elif task == "increment_and_decrement":
    n = int(input())
    for k in range(1, n+1):
        inc = "".join(str(i) for i in range(1, k+1))
        dec = "".join(str(i) for i in range(k-1, 0, -1))
        print(inc + dec)

else:
    print("Invalid task!")
