# HackerRank - Python - Challenges - IX - Errors and Exceptions


# 1. Errors and Exceptions - Exceptions
#
# Exceptions (https://docs.python.org/2/tutorial/errors.html#exceptions)
#
# Errors detected during execution are called exceptions.
#
# Examples:
#
# ZeroDivisionError
# This error is raised when the second argument of a division or modulo operation is zero.
#
>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero
#
# ValueError
# This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
#
>>> a = '1'
>>> b = '#'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10: '#'
#
# To learn more about different built-in exceptions click here. (https://docs.python.org/2/library/exceptions.html#module-exceptions)
#
# Handling Exceptions
#
# The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to specify handlers for different exceptions.
#

#Code

try:
    print 1/0
except ZeroDivisionError as e:
    print "Error Code:",e
#
# Output
#
# Error Code: integer division or modulo by zero
#
# Task
#
# You are given two values a and b.
# Perform integer division and print.
#
# Input Format
#
# The first line contains, the number of test cases.
# The next T lines each contain the space separated values of a and b.
#
# Constraints
#
# 0 < T < 10
#
# Output Format
#
# Print the value of a/b.
# In the case of ZeroDivisionError or ValueError, print the error code.
#
# Sample Input
#
 3 
 1 0 
 2 $ 
 3 1 
#
# Sample Output
#
 Error Code: integer division or modulo by zero 
 Error Code: invalid literal for int() with base 10: '$' 
 3 
#
# Note:
#
# For integer division in Python 3 use //.
#
# Solution

for __ in range(int(input())):
    a, b = input().split()
    try:
        a, b = int(a), int(b)
        quotient: int = a // b
    except (ValueError, ZeroDivisionError) as e:
        print("Error Code:", e)
    else:
        print(quotient)


# 2. Errors and Exceptions - Incorrect Regex
#
# You are given a string S.
# Your task is to find out whether S is a valid regex or not. (https://en.wikipedia.org/wiki/Regular_expression)
#
# Input Format
#
# The first line contains integer T, the number of test cases.
# The next lines contains the string S.
#
# Constraints
#
# 0 < T < 10
#
# Output Format
#
# Print "True" or "False" for each test case without quotes.
#
# Sample Input
#
 2 
 .*\+ 
 .*+ 
#
# Sample Output
#
 True 
 False 
#
# Explanation
#
# .*\+ : Valid regex.
# .*+: Has the error multiple repeat. Hence, it is invalid.
#
# Solution
#

import re

for __ in range(int(input())):
    try:
        re.compile(input())
    except:
        print(False)
    else:
        print(True)

 
