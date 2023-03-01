# HackerRank - Python - Challenges - III - Strings


# 1. Strings - sWAP cASE
#
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#
# For Example:
#
 Www.HackerRank.com → wWW.hACKERrANK.COM 
 Pythonist 2 → pYTHONIST 2 
#
# Function Description
#
# Complete the swap_case function in the editor below.
# swap_case has the following parameters:
# - string s: the string to modify
#
# Returns
#
# - string: the modified string
#
# Input Format
#
# A single line containing a string s.
#
# Constraints
#
# 0 < len(s) ≤ 1000
#
# Sample Input 0
#
 HackerRank.com presents "Pythonist 2". 
#
# Sample Output 0
#
 hACKERrANK.COM PRESENTS "pYTHONIST 2". 
#
# Solution
#

def swap_case(s):
    word = [letter.lower() if letter.isupper() else 
            letter.upper() if letter.islower() else letter
            for letter in s]
    return ''.join(word)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# 2. Strings - String Split and Join
#
# In Python, a string can be split on a delimiter.
#
# Example:
#
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']
#
# Joining a string is simple:
#
>>> a = "-".join(a)
>>> print a
this-is-a-string 
#
# Task
#
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
#
# Function Description
#
# Complete the split_and_join function in the editor below.
# split_and_join has the following parameters:
# - string line: a string of space-separated words
#
# Returns
#
# - string: the resulting string
#
# Input Format
#
# The one line contains a string consisting of space separated words.
#
# Sample Input
#
 this is a string 
#
# Sample Output
#
 this-is-a-string 
#
# Solution
#

def split_and_join(line):
    # write your code here
    newline = line.split(" ")
    return "-".join(newline)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# 3. Strings - What's Your Name?
#
# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
#
 Hello firstname lastname! You just delved into python. 
#
# Function Description
#
# Complete the print_full_name function in the editor below.
# print_full_name has the following parameters:
# - string first: the first name
# - string last: the last name
#
# Prints
#
# - string: 'Hello firstname lastname! You just delved into python' where firstname and lastname are replaced with first and last.
#
# Input Format
#
# The first line contains the first name, and the second line contains the last name.
#
# Constraints
#
# The length of the first and last names are each ≤ 10.
#
# Sample Input 0
#
 Ross 
 Taylor 
#
# Sample Output 0
#
 Hello Ross Taylor! You just delved into python. 
#
# Explanation 0
#
# The input read by the program is stored as a string data type. A string is a collection of characters.
#
# Solution
#

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print("Hello " + first + " " + last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# 4. Strings - Mutations
#
# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
#
# Let's try to understand this with an example.
# You are given an immutable string, and you want to make changes to it.
#
# Example
#
>>> string = "abracadabra"
#
# You can access an index by:
#
>>> print string[5]
a
#
# What if you would like to assign a value?
#
>>> string[5] = 'k' 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
#
# How would you approach this?
# - One solution is to convert the string to a list and then change the value.
#
# Example
#
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
#
# - Another approach is to slice the string and join it back.
#
# Example
#
>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
#
# Task
# Read a given string, change the character at a given index and then print the modified string.
#
# Function Description
#
# Complete the mutate_string function in the editor below.
# mutate_string has the following parameters:
# - string string: the string to change
# - int position: the index to insert the character at
# - string character: the character to insert
#
# Returns
#
# - string: the altered string
#
# Input Format
#
# The first line contains a string, string.
# The next line contains an integer position, the index location and a string character, separated by a space.
#
# Sample Input
#
 STDIN           Function 
 -----           -------- 
 abracadabra     s = 'abracadabra' 
 5 k             position = 5, character = 'k' 
#
# Sample Output
#
# abrackdabra
#
# Solution
#

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# 5. Strings - Find a string
#
# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
#
# NOTE: String letters are case-sensitive.
#
# Input Format
#
# The first line of input contains the original string. The next line contains the substring.
#
# Constraints
#
# 1 ≤ len(string) ≤ 200 
#
# Each character in the string is an ascii character.
#
# Output Format
#
# Output the integer number indicating the total number of occurrences of the substring in the original string.
#
# Sample Input
#
 ABCDCDC 
 CDC 
#
# Sample Output
#
 2 
#
# Concept
#
# Some string processing examples, such as these, might be useful. (https://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-12--string-manipulation)
#
# There are a couple of new concepts:
# In Python, the length of a string is found by the function len(s), where s is the string.
# To traverse through the length of a string, use a for loop:
#
for i in range(0, len(s)):
    print (s[i])
#
# A range function is used to loop over some length:
#
range (0, 5)
#
# Here, the range loops over 0 to 4. 5 is excluded.
#
# Solution
#

def count_substring(string, sub_string):
    n = 0
    for i in range(len(string)):
        if string[i: i+len(sub_string)] == sub_string:
            n+= 1
    return n

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# 6. Strings - String Validators
#
# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
#
# str.isalnum() (https://docs.python.org/2/library/stdtypes.html#str.isalnum)
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
#
>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
#
# str.isalpha() (https://docs.python.org/2/library/stdtypes.html#str.isalpha)
# This method checks if all the characters of a string are alphabetical (a-z and A-Z).
#
>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
#
# str.isdigit() (https://docs.python.org/2/library/stdtypes.html#str.isdigit)
# This method checks if all the characters of a string are digits (0-9).
#
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
#
# str.islower() (https://docs.python.org/2/library/stdtypes.html#str.islower)
# This method checks if all the characters of a string are lowercase characters (a-z).
#
>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
#
# str.isupper() (https://docs.python.org/2/library/stdtypes.html#str.isupper)
# This method checks if all the characters of a string are uppercase characters (A-Z).
#
>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
#
# Task
#
# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
#
# Input Format
#
# A single line containing a string S.
#
# Constraints
#
# 0 < len(S) < 1000
#
# Output Format
#
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
#
# Sample Input
#
 qA2 
#
# Sample Output
#
 True 
 True 
 True 
 True 
 True 
#
# Solution
#

if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


# 7. Strings - Text Alignment
#
# In Python, a string of text can be aligned left, right and center.
#
# .ljust(width)
# This method returns a left aligned string of length width.
#
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  
#
# .center(width)
# This method returns a centered string of length width.
#
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
#
# .rjust(width)
# This method returns a right aligned string of length width.
#
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
#
# Task
#
# You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
# Your task is to replace the blank (______) with rjust, ljust or center.
#
# Input Format
#
# A single line containing the thickness value for the logo.
#
# Constraints
#
# The thickness must be an odd number.
# 0 < thickness < 50
#
# Output Format
#
# Output the desired logo.
#
# Sample Input
#
 5 
#
# Sample Output
#
     H    
    HHH   
   HHHHH  
  HHHHHHH 
 HHHHHHHHH 
   HHHHH               HHHHH             
   HHHHH               HHHHH             
   HHHHH               HHHHH             
   HHHHH               HHHHH             
   HHHHH               HHHHH             
   HHHHH               HHHHH             
   HHHHHHHHHHHHHHHHHHHHHHHHH   
   HHHHHHHHHHHHHHHHHHHHHHHHH   
   HHHHHHHHHHHHHHHHHHHHHHHHH   
   HHHHH               HHHHH             
   HHHHH               HHHHH             
   HHHHH               HHHHH             
   HHHHH               HHHHH             
   HHHHH               HHHHH             
   HHHHH               HHHHH             
                     HHHHHHHHH 
                      HHHHHHH  
                       HHHHH   
                        HHH    
                         H 
#
# Solution
#

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# 8. Strings - Text Wrap
#
# Check Tutorial tab to know how to to solve. (https://www.hackerrank.com/challenges/text-wrap/tutorial)
#
# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.
#
# Function Description
#
# Complete the wrap function in the editor below.
# wrap has the following parameters:
# - string string: a long string
# - int max_width: the width to wrap to
#
# Returns
#
# - string: a single string with newline characters ('\n') where the breaks should be
#
# Input Format
#
# The first line contains a string, string.
# The second line contains the width, max_width.
#
# Constraints
#
# 0 < len(string) < 1000
# 0 < max_width < len(string)
#
# Sample Input 0
#
 ABCDEFGHIJKLIMNOQRSTUVWXYZ 
 4 
#
# Sample Output 0
#
 ABCD 
 EFGH 
 IJKL 
 IMNO 
 QRST 
 UVWX 
 YZ 
#
# Solution
#

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# 9. Strings - Designer Door Mat
#
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
# - Mat size must be N x M. (N is an odd natural number, and is 3 times N.)
# - The design should have 'WELCOME' written in the center.
# - The design pattern should only use |, . and - characters.
#
# Sample Designs
#
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
#
# Input Format
#
# A single line containing the space separated values of N and M.
#
# Constraints
#
# 0 < N < 101
# 15 < M < 303
#
# Output Format
#
# Output the design pattern.
#
# Sample Input
#
 9 27 
#
# Sample Output
#
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
#
# Solution
#

N, M = map(int, input().split())

carac = ".|."
fill = "-"
middle = N//2
fac = 1

for x in range(N):
    if x < middle:
        print((carac*fac).center(M, fill))
        fac += 2
    elif x > middle:
        fac -= 2
        print((carac*fac).center(M, fill))
    else:
        print("WELCOME".center(M, fill))


# 10. Strings - String Formatting
#
# Given an integer, n, print the following values for each integer i from 1 to n:
#  1.  Decimal
#  2.  Octal
#  3.  Hexadecimal (capitalized)
#  4.  Binary
#
# Function Description
#
# Complete the print_formatted function in the editor below.
# print_formatted has the following parameters:
# - int number: the maximum value to print
#
# Prints
#
# The four values must be printed on a single line in the order specified above for each i from 1 to number. Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.
#
# Input Format
#
# A single integer denoting n.
#
# Constraints
#
# 1 ≤ n ≤ 99
#
# Sample Input
#
 17 
#
# Sample Output
#
    1     1     1     1 
    2     2     2    10 
    3     3     3    11 
    4     4     4   100 
    5     5     5   101 
    6     6     6   110 
    7     7     7   111 
    8    10     8  1000 
    9    11     9  1001 
   10    12     A  1010 
   11    13     B  1011 
   12    14     C  1100 
   13    15     D  1101 
   14    16     E  1110 
   15    17     F  1111 
   16    20    10 10000 
   17    21    11 10001 
#
# Solution
#

def print_formatted(number):
    # your code goes here
    maximum = len(str(bin(number)[2:]))
    
    def format_string(item):
        return str(item).upper().rjust(maximum," ")
        
    for i in range(1,number+1):
        num = format_string(i)
        octo = format_string(oct(i)[2:])
        hexo = format_string(hex(i)[2:])
        bino = format_string(bin(i)[2:])
        print(f"{num} {octo} {hexo} {bino}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# 11. Strings - Alphabet Rangoli
#
# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
#
# Different sizes of alphabet rangoli are shown below:
#
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
#
# The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).
#
# Function Description
#
# Complete the rangoli function in the editor below.
# rangoli has the following parameters:
# - int size: the size of the rangoli
#
# Returns
# - string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
#
# Input Format
#
# Only one line of input containing size, the size of the rangoli.
#
# Constraints
#
# 0 < size < 27
#
# Sample Input
#
 5 
#
# Sample Output
#
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
#
# Solution
#

def print_rangoli(size):
    # your code goes here
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    middle_ini = alphabets[1:size][::-1] + alphabets[0:size]
    current_str = ("-").join(list(middle_ini))
    res = current_str

    for i in range(size-1):
        next_str = current_str.replace(
        current_str[(size*2) - 2 : (size*2) + 2 ], "").center(
            len(current_str),"-")
        res = next_str+"\n"+res+"\n"+next_str
        current_str = next_str
        
    print(res)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# 12. Strings - Capitalize!
#
# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
#
# alison heck => Alison Heck
#
# Given a full name, your task is to capitalize the name appropriately.
#
# Input Format
#
# A single line of input containing the full name, S.
#
# Constraints
#
# 0 < len(S) < 1000
# The string consists of alphanumeric characters and spaces.
#
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
#
# Output Format
#
# Print the capitalized string, S.
#
# Sample Input
#
 chris alan 
#
# Sample Output
#
 Chris Alan 
#
# Solution
#

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l = s.split(" ")
    capitalized = ""
    for i in l:
        capitalized += i.capitalize() + " "
    return capitalized.strip()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# 13. Strings - The Minion Game
#
# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.
#
# For Example:
#
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#
# For better understanding, see the image below:
#
# [/data/The_Minion_Game.png]
#
# (https://s3.amazonaws.com/hr-challenge-images/9693/1450330231-04db904008-banana.png)
#
# Your task is to determine the winner of the game and their score.
#
# Function Description
#
# Complete the minion_game in the editor below.
# minion_game has the following parameters:
# - string string: the string to analyze
#
# Prints
#
# - string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
#
# Input Format
#
# A single line of input containing the string S.
# Note: The string S will contain only uppercase letters: [A-Z].
#
# Constraints
#
# 0 < len(S) ≤ 10^6
#
# Sample Input
#
 BANANA 
#
# Sample Output
#
 Stuart 12 
#
# Note:
#
# Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.
#
# Solution
#

def minion_game(string):
    # your code goes here
    kevin, stuart = 0, 0
    vowels = 'AEIOU'
    n = len(string)
    for i, c in enumerate(string):
        if vowels.find(c) != -1:
            kevin += n - i
        else:
            stuart += n - i
    if kevin - stuart != 0:
        print(f'Kevin {kevin}' if kevin > stuart else f'Stuart {stuart}')
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)


# 14. Strings - Merge the Tools!
#
# Consider the following:
# - A string, s, of length n where s = c_0 c_1 ... c_n-1 .
# - An integer, k, where k is a factor of n.
#
# We can split s into n/k substrings where each subtring, t_i , consists of a contiguous block of k characters in s. Then, use each t_i to create string u_i such that:
# - The characters in u_i are a subsequence of the characters in t_i .
# - Any repeat occurrence of a character is removed from the string such that each character in u_i occurs exactly once. In other words, if the character at some index j in t_i occurs at a previous index < j in t_i , then do not include the character in string u_i.
#
# Given s and k, print n/k lines where each line i denotes string u_i.
#
# Example
#
# s = 'AAABCADDE'
# k = 3
#
# There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so . The second substring has all distinct characters, so u_2 = 'BCA'. The third substring has different characters, so u_1 = 'A'. Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.
#
# Function Description
#
# Complete the merge_the_tools function in the editor below.
# merge_the_tools has the following parameters:
# - string s: the string to analyze
# - int k: the size of substrings to analyze
#
# Prints
#
# Print each subsequence on a new line. There will be n/k of them. No return value is expected.
#
#
# Input Format
#
# The first line contains a single string, s.
# The second line contains an integer, k, the length of each substring.
#
# Constraints
#
# 1 ≤ n ≤ 10^4, where n is the length of s
# 1 ≤ k ≤ n
# It is guaranteed that is a multiple of k.
#
# Sample Input
#
 STDIN       Function 
 -----       -------- 
 AABCAAADA   s = 'AABCAAADA' 
 3           k = 3 
#
# Sample Output
#
 AB 
 CA 
 AD 
#
# Explanation
#
# Split s into n/k = 9/3 = 3 equal parts of length k = 3. Convert each t_i to u_i by removing any subsequent occurrences of non-distinct characters in t_i:
#
# 1. t_0 = "AAB" -> u_0 = "AB"
# 2. t_1 = "CAA" -> u_0 = "CA"
# 3. t_2 = "ADA" -> u_0 = "AD"
# Print each on a new line.
#
# Solution
#

def merge_the_tools(string, k):
    # your code goes here
    ns=''
    for i,char in enumerate(string,1):
        if char not in ns:
            ns=''.join((ns,char))
        if i%k==0:
            print(ns)
            ns=''

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


