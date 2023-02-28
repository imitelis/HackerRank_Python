# HackerRank - Python - Challenges - I - Introduction


# 1. Introduction - Say "Hello, World!" With Python
#
# Check Tutorial tab to know how to to solve. (https://www.hackerrank.com/challenges/py-hello-world/tutorial)
#
# Here is a sample line of code that can be executed in Python:
#
print("Hello, World!")
#
# You can just as easily store a string as a variable and then print it to stdout:
#
my_string = "Hello, World!"
print(my_string)
#
# The above code will print Hello, World! on your screen. Try it yourself in the editor below!
#
# Input Format
#
# You do not need to read any input in this challenge.
#
# Output Format
#
# Print Hello, World! to stdout.
#
# Sample Output 0
#
 Hello, World! 
#
# Solution
#

print("Hello, World!")


# 2. Introduction - Python If-Else
#
# Check Tutorial tab to know how to to solve. (https://www.hackerrank.com/challenges/py-if-else/tutorial)
#
# Task
#
# Given an integer,, perform the following conditional actions:
# - If n is odd, print Weird
# - If n is even and in the inclusive range of 2 to 5, print Not Weird
# - If n is even and in the inclusive range of 6 to 20, print Weird
# - If n is even and greater than 20, print Not Weird
#
# Input Format
#
# A single line containing a positive integer, n.
#
# Constraints
#
# 1 ≤ n ≤ 100
#
# Output Format
#
# Print Weird if the number is weird. Otherwise, print Not Weird.
#
# Sample Input 0
#
 3 
#
# Sample Output 0
#
 Weird 
#
# Explanation 0
#
# n = 3
# n is odd and odd numbers are weird, so print Weird.
#
# Sample Input 1
#
 24 
#
# Sample Output 1
#
 Not Weird 
#
# Explanation 1
#
# n=24
# n>20 and is even, so it is not weird.
#
# Solution
#

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2 != 0):
        print("Weird")
    else:
        if (n >= 2 and n <= 5):
            print("Not Weird")
        elif (n >= 6 and n <= 20):
            print("Weird")
        elif (n > 20):
            print("Not Weird")


# 3. Introduction - Arithmetic Operators
#
# Check Tutorial tab to know how to to solve. (https://www.hackerrank.com/challenges/python-arithmetic-operators/tutorial)
#
# Task
#
# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
# - The first line contains the sum of the two numbers.
# - The second line contains the difference of the two numbers (first - second).
# - The third line contains the product of the two numbers.
#
# Example
#
# a = 3
# b = 5
#
# Print the following:
#
 8 
 -2 
 15 
#
# Input Format
#
# The first line contains the first integer, a.
# The second line contains the second integer, b.
#
# Constraints
#
# 1 ≤ a ≤ 10^10
# 1 ≤ b ≤ 10^10
#
#
# Output Format
#
# Print the three lines as explained above.
#
# Sample Input 0
#
 3 
 2 
#
# Sample Output 0
#
 5 
 1 
 6 
#
# Explanation 0
#
# 3+2 => 5
# 3-2 => 1
# 3*2 => 6
#
# Solution
#

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)


# 4. Introduction - Python: Division
#
# Check the Tutorial tab to know learn about division operators. (https://www.hackerrank.com/challenges/python-division/tutorial)
#
# Task
#
# The provided code stub reads two integers, a and b, from STDIN.
#
# Add logic to print two lines. The first line should contain the result of integer division, a//b. The second line should contain the result of float division, a/b.
#
# No rounding or formatting is necessary.
#
# Example
#
# a = 3
# b = 5
#
# - The result of the integer division 3//5=0.
# - The result of the float division is 3/5=0.6.
#
# Print:
#
 0 
 0.6 
#
# Input Format
#
# The first line contains the first integer, a.
# The second line contains the second integer, b.
#
# Output Format
#
# Print the two lines as described above.
#
# Sample Input 0
#
 4 
 3 
#
# Sample Output 0
#
 1 
 1.33333333333 
#
# Solution
#

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)


# 5. Introduction - Loops
#
# Check Tutorial tab to know how to to solve. (https://www.hackerrank.com/challenges/python-loops/tutorial)
#
# Task
#
# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i.
#
# Example
# 
# n = 3
# The list of non-negative integers that are less than n=3 is [0,1,2]. Print the square of each number on a separate line.
#
 0 
 1 
 4 
#
# Input Format
#
# The first and only line contains the integer, n.
#
# Constraints
#
# 1 ≤ n ≤ 20
#
# Output Format
#
# Print n lines, one corresponding to each i.
#
# Sample Input 0
#
 5 
#
# Sample Output 0
#
 0 
 1 
 4 
 9 
 16 
#
# Solution
#

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i)


# 6. Introduction - Write a function
#
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
#
# In the Gregorian calendar, three conditions are used to identify leap years:
#
# - The year can be evenly divided by 4, is a leap year, unless:
#   - The year can be evenly divided by 100, it is NOT a leap year, unless:
#     - The year is also evenly divisible by 400. Then it is a leap year.
#
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source (https://www.timeanddate.com/date/leapyear.html)
#
# Task
#
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
#
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
#
# Input Format
#
# Read year, the year to test.
#
# Constraints
#
# 1900 ≤ year ≤ 10^5
#
# Output Format
#
# The function must return a Boolean value (True/False). Output is handled by the provided code stub.
#
# Sample Input 0
#
 1990 
#
# Sample Output 0
#
 False 
#
# Explanation 0
#
# 1990 is not a multiple of 4 hence it's not a leap year. 
#
# Solution
#

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:
        leap = True
    if year%100 == 0:
        if year%400 != 0:
            leap = False
    return leap

year = int(input())
print(is_leap(year))


# 7. Introduction - Print Function
#
# Check Tutorial tab to know how to to solve. (https://www.hackerrank.com/challenges/python-print/tutorial)
#
# The included code stub will read an integer, n, from STDIN.
#
# Without using any string methods, try to print the following:
# 123 ⋅⋅⋅ n
#
# Note that "⋅⋅⋅" represents the consecutive values in between.
#
# Example
#
# n = 5
# Print the string 12345.
#
# Input Format
#
# The first line contains an integer.
#
# Constraints
#
# 1 ≤ n ≤ 150
#
# Output Format
#
# Print the list of integers from through as a string, without spaces.
#
# Sample Input 0
#
 3 
#
# Sample Output 0
#
 123 
#
# Solution
#

if __name__ == '__main__':
    n = int(input())
    n_string = ""
    for i in range(1,n+1):
        print(i, end="")


