# Tasks and Goals

# Accumulation - Accumulating a final result
  # sum_until_0: Continuously read integers from standard input until you receive a zero. Print the sum of these integers.
  #total_price: Continuously read pairs of integers from standard input, representing the quantity and price of items, until you receive the string "END". Print the total price of all items.

# Filtering - Selecting based on a criterion
  # only_ed_or_ing: Continuously read strings from standard input until you encounter the word "STOP" (case insensitive and not included in the output). Print only those strings that end with "ed" or "ing" (case insensitive).
  # reverse_sum_palindrome: Continuously read positive integers from standard input until you encounter a "-1"(not included in the output). Print only those integers for which the sum of the number and its reverse is a palindrome.

# Mapping - Applying the same operation to different items
  # double_string: Continuously read lines from standard input until an empty line is encountered. Print each line repeated twice.
  # odd_char: Continuously read strings from standard input until you encounter a string ending with a "."(include that string with the "." in the output). Extract characters at odd positions (starting from 1) of each line, and print the results in a single line separated by spaces.

# Filter and Map - Applying an operation to selected items
  # only_even_squares: Continuously read numbers from standard input until "NAN" is encountered. Print the square of each number only if it is even.

# Filter and Accumulate - Accumulating a result with selected items
  #only_odd_lines: Continuously read lines from standard input until "END"(not included in the output) is encountered. Create a string by prepending only the odd lines (starting from 1) with a newline character in between, and print the result which will be the odd lines in reverse order.


task = input()

if task == "sum_until_0":
    total = 0
    while True: # the terminal condition
        n = int(input())
        if n == 0:
            break
        if n != 0:
            total = total + n   # add n to the total
    print(total)                # take the next n form the input
        

elif task == "total_price":
    total_price = 0
    while total_price >= 0: # repeat forever since we are breaking inside
        line = input()
        if line == 'END': # The terminal condition
            break
        quantity, price = line.split() # split uses space by default
        quantity, price = int(quantity), int(price) # convert to ints
        total_price = total_price + (quantity*price) # accumulate the total price
    print(total_price)


elif task == "only_ed_or_ing":
   while True:
    string = input()
    if string == "":  
        break
    if string[-2:] == "ed" or string[-3:] == "ing":
        print(string)


elif task == "reverse_sum_palindrome":
    while True:
        num = int(input())
        if num == -1:
            break
        else:
            rnum = str(num)[::-1]
            sum = num + int(rnum)
            rsum = str(sum)[::-1]
            if sum == int(rsum):
                print(num)
        

elif task == "double_string":
    while True:
        line = input()
        if line == " ":
            break
        else:
            print(line+line)
        

elif task == "odd_char":
    results=[]
    while True:
        s = input()
        results.append(s[::2])  # odd positions (starting from 1, i.e., indices 0,2,4,...)
        if s.endswith("."):
            break

    print(" ".join(results))


elif task == "only_even_squares":
    while True:
        num = input()
        if (int(num)%2==0):
            print(int(num)*int(num))
        elif (num == "NAN"):
            break


elif task == "only_odd_lines":
    result = ""
    lines = []
    count = 1  # line number

    while True:
        s = input()
        if s == "END":
            break
        if count % 2 == 1:  # odd-numbered line
            lines.insert(0, s)  # prepend to the list to reverse order
        count += 1

# Combine all lines into a single string with newlines
    result = "\n".join(lines)
    print(result)
