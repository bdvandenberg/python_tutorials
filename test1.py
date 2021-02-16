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
import numpy as np
import pandas as pd
import xarray as xr

def oddeven(number):
    if number % 2 == 0:
        output = True
    else:
        output = False
    print(f'output is {output}')

oddeven(2)
