'''
Fibonacci likes to climb the steps either one at a time, two at a time or three at a time. 
This adds variety to the otherwise monotonous task of climbing. 
He wants to find the total number of ways in which he can climb n steps, assuming that the order of his individual steps matters. 
Your task is to help Fibonacci compute this number.

For example, if he wishes to climb three steps, the case of n=3, he could do it in four different ways:
(1,1,1): do it in three moves, one step at a time
(1,2): do it in two moves, first take a single step, then a double step
(2,1): do it in two moves, first take a double step, then a single step
(3): do it in just one move, directly leaping to the third step

Write a recursive function named steps that accepts a positive integer n as argument. 
It should return the total number of ways in which Fibonacci can ascend n steps. 
Note that the order of his steps is important.
'''

def steps(n):
    """
    A recursive function to compute the number of ways to ascend steps 

    Argument:
        n: integer
    Return:
        result: integer
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    return steps(n-1) + steps(n-2) + steps(n-3)
