# weekly task 06
# Write a program that takes a positive floating-point number as input 
# and outputs an approximation of its square root.
# "Create your own sqrt function and not use the built in functions x ** .5 
#  or math.sqrt(x)"
# Author: Dave Byrne :)

"""
Research:
I looked online through Medium and Stackoverflow for references for creating a function
to calculate the square root of a number. I found the following references:
https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm
This led me to investigate the Newton-Raphson method in greater detail:
https://www.geeksforgeeks.org/newton-raphson-method/
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
"""

# define the function

def sqrt(num, tolerance = 1e-6): # did not understand tolerance, deepseek helped me understand
    # num is the number to formulate the square root
    if num < 0:
        raise ValueError("Will not accept a negative integer") # raises error if the number is negative
    
    guess = num / 2 # initial guess - first step of the method

    while True: # Begin loop of formula
        new_guess = 0.5 * (guess + num / guess) # applying the newton-raphson formula
        if abs(new_guess - guess) < tolerance: # abs returns the absolute value of a number, helpful for complex numbers; source: python 3 documentation
            return new_guess
        guess = new_guess

# test function
