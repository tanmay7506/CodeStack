# Operation names:

# odd_num_check: checks whether an integer is odd or not(even)

# perfect_square_check: checks whether an integer is a perfect sqaure or not

# vowel_check: checks whether a string has atleast one vowel

# divisibility_check: checks whether an integer is divisible by both 2 and 3, or only by 2, or only by 3, or by neither

# palindrominator: takes a string and joins it with the same string reversed. Eg. "cal" -> "calac".

# simple_interest: simple interest calculator with inputs with a higher interest rate if long term

import math

operation = input() # input operation name

if (operation == "odd_num_check"):  # checks whether an integer is odd or not(even)
    num = int(input())  # input integer
    
    if(num%2 != 0):
        print("yes")  # prints 'yes' if number is odd
    
    else:
        print("no")  # prints 'no' if number is even
    

elif (operation == "perfect_square_check"):  # checks whether an integer is a perfect sqaure or not
    num = int(input())  # input integer
    
    if(num >= 0 and num//(num**0.5) == num**0.5):
        print("yes")  # prints 'yes' if number is a perfect sqaure
    
    else:
        print("no")  # prints 'no' if number is not a perfect square


elif (operation == "vowel_check"):  # checks whether a string has atleast one vowel
    word = str(input())  # imput string
    vowel = "AaEeIiOoUu"
    
    if any(char in vowel for char in word):
        print("yes")  # prints 'yes' if string has at least one vowel
    
    else:
        print("no")  # prints 'no' if string has no vowel
        

elif (operation == "divisibility_check"):  # checks whether an integer is divisible by both 2 and 3, or only by 2, or only by 3, or by neither
    num = int(input())  # input integer
    
    if (num%2 == 0 and num%3 == 0):
        print("divisible by 2 and 3")  # integer is divisible by 2 and 3
    
    elif (num%2 == 0):
        print("divisible by 2")  # integer is divisible by only 2
    
    elif (num%3 == 0):
        print("divisible by 3")  # integer is divisible by only 3
    
    else:
        print("not divisible by 2 and 3") # integer is divisible neither by 2 nor 3
        

elif (operation == "palindrominator"):  # takes a string and joins it with the same string reversed. Eg. "cal" -> "calac".
   word = str(input())  # input string
   palindrominator = word[0:-1] + word[::-1]  # creates a palindrome
   
    print(palindrominator)  # prints the palindrome
   

elif(operation == "simple_interest"):  # simple interest calculator with inputs with a higher interest rate if long term
    principal_amount = int(input())  # input principal amount
    n_years = int(input())  # input number of years (tenure)
   
    if (0 < n_years < 10):
        simple_interest = round(principal_amount*n_years*5/100)  # 5% p.a. interest if tenure is short term (less than 10 years)
    
    elif(n_years >= 10):
        simple_interest = round(principal_amount*n_years*8/100)  # 8% p.a. interest if tenure is long term (10 or more years)

    print(simple_interest)  # prints simple interest
