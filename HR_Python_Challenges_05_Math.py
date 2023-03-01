# HackerRank - Python - Challenges - V - Math


# 1. Math - Polar Coordinates
#
# Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers. (https://en.wikipedia.org/wiki/Complex_number)
#
# A complex number z
# z = x+yj
# is completely determined by its real part x and imaginary part y.
# Here, j is the imaginary unit. (https://en.wikipedia.org/wiki/Imaginary_unit)
#
# A polar coordinate (r, φ)
#
# [/data/Polar_Coordinates.png]
#
# (https://s3.amazonaws.com/hr-challenge-images/9951/1440141121-5b051fd241-Capture.PNG)
#
# is completely determined by modulus r and phase angle φ.
#
# If we convert complex number z to its polar coordinate, we find:
# r: Distance from z to origin, i.e., √x^2+y^2
# φ: Counter clockwise angle measured from the positive x-axis to the line segment that joins z to the origin.
#
# Python's cmath module provides access to the mathematical functions for complex numbers. (https://docs.python.org/2/library/cmath.html)
#
# cmath.phase
# This tool returns the phase of complex number z (also known as the argument of z).
#
>>> phase(complex(-1.0, 0.0))
 3.1415926535897931 
#
# abs
# This tool returns the modulus (absolute value) of complex number z.
#
>>> abs(complex(-1.0, 0.0))
 1.0 
#
# Task
# You are given a complex z. Your task is to convert it to polar coordinates.
#
# Input Format
#
# A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.
#
# Constraints
#
# Given number is a valid complex number
#
# Output Format
#
# Output two lines:
# The first line should contain the value of r.
# The second line should contain the value of φ.
#
# Sample Input
#
 1+2j 
#
# Sample Output
#
 2.23606797749979 
 1.1071487177940904 
#
# Note: The output should be correct up to 3 decimal places.
#
# Solution
#

import cmath;

z = complex(input())

print(cmath.polar(z)[0])
print(cmath.polar(z)[1])


# 2. Math - Find Angle MBC
#
# [/data/Find_Angle_MBC.png]
#
# (https://s3.amazonaws.com/hr-challenge-images/9668/1440151155-10b2b748ee-rsz_1438840048-2cf71ed69d-findangle.png)
#
# ABC is a right triangle, 90° at B.
# Therefore, ∠ABC=90°.
#
# Point M is the midpoint of hypotenuse AC.
# You are given the lengths AB and BC. Your task is to find ∠MBC (angle θ°, as shown in the figure) in degrees.
#
# Input Format
#
# The first line contains the length of side AB.
# The second line contains the length of side BC.
#
# Constraints
#
# 0 < AB ≤ 100
# 0 < BC ≤ 100
# Lengths AB and BC are natural numbers.
#
# Output Format
#
# Output ∠MBC in degrees.
# Note: Round the angle to the nearest integer.
#
# Examples:
#
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.
#
# 0° < θ° < 90°
#
# Sample Input
#
 10 
 10 
#
# Sample Output
#
 45° 
#
# Solution
#

import sys
import math

def find_angle (m,n):
    angle = round(math.degrees(math.atan(m / n)))
    return angle

if __name__ == "__main__":
    AB = int(input())
    BC = int(input())
    print(str(str(find_angle(AB, BC))) + chr(176))


# 3. Math - Triangle Quest 2
#
# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.
#
# For example, a palindromic triangle of size 5 is:
#
 1 
 121 
 12321 
 1234321 
 123454321 
#
# You can't take more than two lines. The first line (a for-statement) is already written for you.
# You have to complete the code using exactly one print statement.
#
# Note:
#
# Using anything related to strings will give a score of 0.
# Using more than one for-statement will give a score of 0.
#
# Input Format
#
# A single line of input containing the integer N.
#
# Constraints
#
# 0 < N < 10
#
# Output Format
#
# Print the palindromic triangle of size as explained above.
#
# Sample Input
#
 5 
#
# Sample Output
#
 1 
 121 
 12321 
 1234321 
 123454321 
#
# Solution
#

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i-1)//9)**2)


# 4. Math - Mod Divmod
#
# One of the built-in functions of Python is divmod, which takes two arguments a and b and returns a tuple containing the quotient of a/b first and then the remainder a.
#
# For example:
#
>>> print divmod(177,10)
 (17, 7) 
#
# Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.
#
# Task
#
# Read in two integers, a and b, and print three lines.
# The first line is the integer division a//b (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: a%b.
# The third line prints the divmod of a and b.
#
# Input Format
#
# The first line contains the first integer, a, and the second line contains the second integer, b.
#
# Output Format
#
# Print the result as described above.
#
# Sample Input
#
 177 
 10 
#
# Sample Output
#
 17 
 7 
 (17, 7) 
#
# Solution
#

if __name__ == "__main__":
    a, b = int(input()), int(input())
    print(a//b)
    print(a%b)
    print(divmod(a,b))


# 5. Math - Power - Mod Power
#
# So far, we have only heard of Python's powers. Now, we will witness them!
# Powers or exponents in Python can be calculated using the built-in power function. Call the power function a^b as shown below:
#
>>> pow(a,b) 
#
# or
#
>>> a**b
#
# It's also possible to calculate a^b mod m.
#
>>> pow(a,b,m)  
#
# This is very helpful in computations where you have to print the resultant % mod.
#
# Note: Here, a and b can be floats or negatives, but, if a third argument is present, b cannot be negative.
#
# Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. It is uncommon to use math.pow().
#
# Task
#
# You are given three integers: a, b, and m. Print two lines.
# On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).
#
# Input Format
#
# The first line contains , the second line contains b, and the third line contains m.
#
# Constraints
#
# 1 ≤ a ≤ 10
# a ≤ b ≤ 10
# 2 ≤ m ≤ 1000
#
# Sample Input
#
 3 
 4 
 5 
#
# Sample Output
#
 81 
 1 
#
# Solution
#

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    m = int(input())
    print(pow(a,b))
    print(pow(a,b,m))


# 6. Math - Integers Come In All Sizes
#
# Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: 2^(31)-1 (c++ int) or 2^(63)-1 (C++ long long int).
# As we know, the result of a^b grows really fast with increasing b.
# Let's do some calculations on very large integers.
#
# Task
# Read four numbers, a, b, c, and d, and print the result of (a^b)+(c^d).
#
# Input Format
#
# Integers a, b, c, and d are given on four separate lines, respectively.
#
# Constraints
#
# 1 ≤ a ≤ 1000
# 1 ≤ b ≤ 1000
# 1 ≤ c ≤ 1000
# 1 ≤ d ≤ 1000
#
# Output Format
#
# Print the result of (a^b)+(c^d) on one line.
#
# Sample Input
#
 9 
 29 
 7 
 27 
#
# Sample Output
#
 4710194409608608369201743232 
#
# Note: This result is bigger than 2^(63)-1. Hence, it won't fit in the long long int of C++ or a 64-bit integer.
#
# Solution
#

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(pow(a,b)+pow(c,d))


# 7. Math - Triangle Quest
#
# You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:
#
 1 
 22 
 333 
 4444 
 55555 
 ...... 
#
# Can you do it using only arithmetic operations, a single for loop and print statement?
# Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.
#
# Note: Using anything related to strings will give a score of 0.
#
# Input Format
#
# A single line containing integer, N.
#
# Constraints
#
# 1 ≤ N ≤ 9
#
# Output Format
#
# Print N-1 lines as explained above.
#
# Sample Input
#
 5 
#
# Sample Output
#
 1 
 22 
 333 
 4444 
#
# Solution
#

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i-1)//9)*i)


