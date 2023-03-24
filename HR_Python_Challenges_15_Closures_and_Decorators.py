# HackerRank - Python - Challenges - XV - Closures and Decorators


# 1. Closures and Decorators - Standardize Mobile Number Using Decorators
#
# Let's dive into decorators! You are given N mobile numbers. Sort them in ascending order then print them in the standard format shown below:
#
 +91 xxxxx xxxxx 
#
# The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all.
#
# Input Format
#
# The first line of input contains an integer N, the number of mobile phone numbers.
# N lines follow each containing a mobile number.
#
# Output Format
#
# Print N mobile numbers on separate lines in the required format.
#
# Sample Input
#
 3 
 07895462130 
 919875641230 
 9195969878 
#
# Sample Output
#
 +91 78954 62130 
 +91 91959 69878 
 +91 98756 41230 
#
# Concept
#
# Like most other programming languages, Python has the concept of closures. Extending these closures gives us decorators, which are an invaluable asset. You can learn about decorators in 12 easy steps here. (http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)
# To solve the above question, make a list of the mobile numbers and pass it to a function that sorts the array in ascending order. Make a decorator that standardizes the mobile numbers and apply it to the function.
#
# Solution
#

def wrapper(f):
    def fun(l):
        l = map(lambda x:f"+91 { x[-10:-5:] } { x[-5::] }", l)
        return f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# 2. Closures and Decorators - Decorators 2 - Name Directory
#
# Let's use decorators to build a name directory! You are given some information about N people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.
#
# For Henry Davids, the output should be:
#
 Mr. Henry Davids 
#
# For Mary George, the output should be:
#
 Ms. Mary George 
#
# Input Format
#
# The first line contains the integer N, the number of people.
# N lines follow each containing the space separated values of the first name, last name, age and sex, respectively.
#
# Constraints
#
# 1 ≤ N ≤ 10
#
# Output Format
#
# Output N names on separate lines in the format described above in ascending order of age.
#
# Sample Input
#
 3 
 Mike Thomson 20 M 
 Robert Bustle 32 M 
 Andria Bustle 30 F 
#
# Sample Output
#
 Mr. Mike Thomson 
 Ms. Andria Bustle 
 Mr. Robert Bustle 
#
# Concept
#
# For sorting a nested list based on some parameter, you can use the itemgetter library. You can read more about it here. (https://stackoverflow.com/questions/409370/sorting-and-grouping-nested-lists-in-python?answertab=votes#tab-top)
#
# Solution
#

import operator

def person_lister(f):
    def inner(people):
        people.sort(key= lambda x: int(x[2]))
        return [f(i) for i in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


