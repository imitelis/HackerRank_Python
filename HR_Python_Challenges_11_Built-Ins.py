# HackerRank - Python - Challenges - XI - Built-Ins


# 1. Built-Ins - Zipped!
#
# zip([iterable, ...]) (https://docs.python.org/2/library/functions.html#zip)
#
# This function returns a list of tuples. The ith tuple contains the ith element from each of the argument sequences or iterables.
#
# If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.
#
# Sample Code
#
>>> print zip([1,2,3,4,5,6],'Hacker')
[(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
>>> 
>>> print zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1])
[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
>>> 
>>> A = [1,2,3]
>>> B = [6,5,4]
>>> C = [7,8,9]
>>> X = [A] + [B] + [C]
>>> 
>>> print zip(*X)
[(1, 6, 7), (2, 5, 8), (3, 4, 9)]
#
# Task
#
# The National University conducts an examination of N students in X subjects.
# Your task is to compute the average scores of each student.
#
# Average score = Sum of scores obtained in all subjects by a student / Total number of subjects
# 
# The format for the general mark sheet is:
#
 Student ID → ___1_____2_____3_____4_____5__ 
 Subject 1   |  89    90    78    93    80 
 Subject 2   |  90    91    85    88    86 
 Subject 3   |  91    92    83    89    90.5 
             |______________________________ 
 Average        90    91    82    90    85.5 
#
# Input Format
#
# The first line contains N and X separated by a space.
# The next X lines contains the space separated marks obtained by students in a particular subject. 
#
# Constraints
#
# 0 < N ≤ 100
# 0 < X ≤ 100
#
# Output Format
#
# Print the averages of all students on separate lines.
# The averages must be correct up to 1 decimal place.
#
# Sample Input
#
 5 3 
 89 90 78 93 80 
 90 91 85 88 86 
 91 92 83 89 90.5 
#
# Sample Output
#
 90.0 
 91.0 
 82.0 
 90.0 
 85.5 
#
# Explanation
#
# Marks obtained by student 1: 89, 90, 91
# Average marks of student 1: 270/3 = 90
#
# Marks obtained by student 2: 90, 91, 92
# Average marks of student 2: 273/3 = 91
#
# Marks obtained by student 3: 78, 85, 83
# Average marks of student 3: 246/3 = 82
#
# Marks obtained by student 4: 93, 88, 89
# Average marks of student 4: 270/3 = 90
# 
# Marks obtained by student 5: 80, 86, 90.5
# Average marks of student 5: 256.5/3 = 85.5
#
# Solution
#

N,X=list(map(int,input().split()))
sub = [(list(map(float,input().split()))) for i in range(X)]
for i in zip(*[sub[i] for i in range(len(sub))]):
    print(sum(i)/len(sub))


# 2. Built-Ins - Input()
#
# input() (https://docs.python.org/2/library/functions.html#input)
#
# In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).
#
# Code
#
>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'
#
# Task
#
# You are given a polynomial P of a single indeterminate (or variable), x. (https://en.wikipedia.org/wiki/Polynomial)
# You are also given the values of x and k. Your task is to verify if P(x) = k.
#
# Constraints
#
# All coefficients of polynomial P are integers.
# x and y are also integers.
#
# Input Format
#
# The first line contains the space separated values of x and k.
# The second line contains the polynomial P.
#
# Output Format
#
# Print True if P(x) = k. Otherwise, print False.
#
# Sample Input
#
 1 4 
 x**3 + x**2 + x + 1 
#
# Sample Output
#
 True 
#
# Explanation
#
# P(1) = 1^3 + 1^2 + 1 + 1 = 4 = k
# Hence, the output is True.
#
# Solution
#

x, k = input().strip().split(' ')
P = input().strip().replace('x',x)
print(eval(P)==int(k))


# 3. Built-Ins - Python Evaluation
#
# The eval() expression is a very powerful built-in function of Python. It helps in evaluating an expression. The expression can be a Python statement, or a code object.
#
# For example:
#
>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5
#
# Here, eval() can also be used to work with Python keywords or defined functions and variables. These would normally be stored as strings.
#
# For example:
#
>>> type(eval("len"))
<type 'builtin_function_or_method'>
#
# Without eval()
#
>>> type("len")
<type 'str'>
#
# Task
# You are given an expression in a line. Read that line as a string variable, such as var, and print the result using eval(var).
#
# NOTE: Python2 users, please import from __future__ import print_function.
#
# Constraint
#
# Input string is less than 100 characters.
#
# Sample Input
#
 print(2 + 3) 
#
# Sample Output
#
 5 
#
# Solution
#

in_str=input()
if len(in_str) <100:
  eval(in_str)


# 4. Built-Ins - Athlete Sort
#
# You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the Kth attribute and print the final resulting table. Follow the example given below for better understanding.
#
# (https://s3.amazonaws.com/hr-assets/0/1514874268-6fabad07aa-AthleteSort2.png)
#
# Note that K is indexed from 0 to M-1, where M is the number of attributes.
#
# Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.
#
# Input Format
#
# The first line contains N and M separated by a space.
# The next N lines each contain M elements.
# The last line contains K.
#
# Constraints
#
# 1 ≤ N, M ≤ 1000
# 0 ≤ K < M
# Each element ≤ 1000
#
# Output Format
#
# Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.
#
# Sample Input 0
#
 5 3 
 10 2 5 
 7 1 0 
 9 9 9 
 1 23 12 
 6 5 9 
 1 
#
# Sample Output 0
#
 7 1 0 
 10 2 5 
 6 5 9 
 9 9 9 
 1 23 12 
#
# Explanation 0
#
# The details are sorted based on the second attribute, since K is zero-indexed. 
#
# Solution
#

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    final_list = list(zip(*arr))
    final_list[k]= list(final_list[k])
    final_list[k].sort()
    L = []
    for i in final_list[k]:
        for j in arr:
            if i == j[k]:
              if j not in L:
                L.append(j)
                print(*j)


# 5. Built-Ins - Any or All
#
# any() (https://docs.python.org/2/library/functions.html#any)
#
# This expression returns True if any element of the iterable is true.
# If the iterable is empty, it will return False.
#
# Code
#
>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False
#
# all() (https://docs.python.org/2/library/functions.html#all)
#
# This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.
#
# Code
#
>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False
#
# Task
#
# You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
#
# Input Format
#
# The first line contains an integer N. N is the total number of integers in the list.
# The second line contains the space separated list of N integers.
#
# Constraints
#
# 0 < N < 100
#
# Output Format
#
# Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.
#
# Sample Input
#
 5 
 12 9 61 5 14 
#
# Sample Output
#
 True 
#
# Explanation
#
# Condition 1: All the integers in the list are positive.
# Condition 2: 5 is a palindromic integer.
#
# Hence, the output is True.
#
# Can you solve this challenge in 3 lines of code or less?
# There is no penalty for solutions that are correct but have more than 3 lines.
#
# Solution
#

count, list_values = input(), input().split()

print (True if all(int(a) >= 0 for a in list_values) and any(int(x [::-1]) == int(x) for x in list_values) else False)


# 6. Built-Ins - ginortS
#
# You are given a string S.
# S contains alphanumeric characters only.
#
# (https://i.imgur.com/u7WkSk7.gif)
#
# Your task is to sort the string S in the following manner:
#  All sorted lowercase letters are ahead of uppercase letters.
#  All sorted uppercase letters are ahead of digits.
#  All sorted odd digits are ahead of sorted even digits.
#
# Input Format
#
# A single line of input contains the string S.
#
# Constraints
#
# 0 < len(S) < 1000
#
# Output Format
#
# Output the sorted string S.
#
# Sample Input
#
 Sorting1234 
#
# Sample Output
#
 ginortS1324 
#
# Solution
#

word = input()

print(''.join(sorted(word, key=lambda x: (x.isdigit(), x.isdigit() and not int(x) % 2, x.isupper(), x,))))


