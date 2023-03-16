# HackerRank - Python - Challenges - XII - Python Functionals


# 1. Python Functionals - Map and Lambda Function
#
# Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers, 0 being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.
#
# Concept
#
# The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables.
# Let's say you are given a list of names, and you have to print a list that contains the length of each name.
#
>> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
[4, 3, 3]  
#
# Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.
#
>> sum = lambda a, b, c: a + b + c
>> sum(1, 2, 3)
6
#
# Note:
#
# Lambda functions cannot use the return statement and can only have a single expression. Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself. Lambda can be used inside lists and dictionaries.
#
# Input Format
#
# One line of input: an integer N.
#
# Constraints
#
# 0 ≤ N ≤ 15
#
#Output Format
#
# A list on a single line containing the cubes of the first N fibonacci numbers.
#
# Sample Input
#
 5 
#
# Sample Output
#
 [0, 1, 1, 8, 27] 
#
# Explanation
#
# The first 5 fibonacci numbers are [0, 1, 1, 2, 3], and their cubes are [0, 1, 1, 8, 27].
#
# Solution
#

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    lst = [0, 1]
    if(n==0): return list()
    if(n==1): return [0]
    if(n==2): return lst
    else:
        for i in range(2, n):
            lst.append(lst[i-1]+lst[i-2])
    return lst


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# 2. Python Functionals - Validating Email Addresses With a Filter
#
# You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.
#
# Valid email addresses must follow these rules:
# - It must have the username@websitename.extension format type.
# - The username can only contain letters, digits, dashes and underscores [a-z], [A-Z], [0-9], [_-].
# - The website name can only have letters and digits [a-z], [A-Z], [0-9].
# - The extension can only contain letters [a-z], [A-Z].
# - The maximum length of the extension is 3.
#
# Concept
#
# A filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence where the function returned True. A Lambda function can be used with filters.
#
# Let's say you have to make a list of the squares of integers from 0 to 9 (both included).
#
>> l = list(range(10))
>> l = list(map(lambda x:x*x, l))
#
# Now, you only require those elements that are greater than 10 but less than 80.
#
>> l = list(filter(lambda x: x > 10 and x < 80, l))
#
# Easy, isn't it?
#
# Example
#
# Complete the function fun in the editor below.
# fun has the following paramters:
# string s: the string to test
#
# Returns
# boolean: whether the string is a valid email or not
#
# Input Format
#
# The first line of input is the integer N, the number of email addresses.
# N lines follow, each containing a string.
#
# Constraints
#
# Each line is a non-empty string.
#
# Sample Input
#
 3 
 lara@hackerrank.com 
 brian-23@hackerrank.com 
 britts_54@hackerrank.com 
#
# Sample Output
#
 ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com'] 
#
# Solution
#

def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, website, extension = s.split("@")[0], *s.split("@")[1].split(".")
    except:
        return False
        
    if "" in [username, website, extension]:
        return False
    
    if len(list(filter(lambda x: not (x.isalnum() or x in "_-"), username))) != 0:
        return False
    
    if len(list(filter(lambda x: not (x.isalnum()), website))) != 0:
        return False
    
    if len(list(filter(lambda x: not (x.isalpha()), extension))) != 0 or len(extension) > 3:
        return False
    
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


# 3. Python Functionals - Reduce Function
#
# Given a list of rational numbers, find their product.
#
# Concept
# The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.
#
>>> reduce(lambda x, y : x + y,[1,2,3])
6
#
# You can also define an initial value. If it is specified, the function will assume initial value as the value given, and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:
#
>>> reduce(lambda x, y : x + y, [1,2,3], -3)
3

>>> from fractions import gcd
>>> reduce(gcd, [2,4,8], 3)
1
#
# Input Format
#
# First line contains n, the number of rational numbers.
# The ith of next n lines contain two integers each, the numerator(N_i) and denominator(D_i) of the ith rational number in the list.
#
# Constraints
#
# 1 ≤ n ≤ 100
# 1 ≤ N_i , D_i ≤ 10^9
#
# Output Format
#
# Print only one line containing the numerator and denominator of the product of the numbers in the list in its simplest form, i.e. numerator and denominator have no common divisor other than 1.
#
# Sample Input 0
#
 3 
 1 2 
 3 4 
 10 6 
#
# Sample Output 0
#
 5 8 
#
# Explanation 0
#
# Required product is 1/2 3/4 10/6 = 5/8
#
# Solution
#

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = Fraction(reduce(lambda x, y : x * y, fracs)) # complete this line with a reduce statement
    return t.numerator, t.denominator
    
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)


