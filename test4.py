"""
Write a function that has the following input and 
output:

Input:
- number

Output:
- True if the number is even, or
- False if the number is odd

Test your function before committing to Github.
"""


def odd_even(number):
    mod = number % 2
    
    print(mod == 0)
    return mod == 0

odd_even(7)
