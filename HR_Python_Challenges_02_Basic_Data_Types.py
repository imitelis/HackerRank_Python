# HackerRank - Python - Challenges - II - Basic Data Types


# 1. Basic Data Types - List Comprehensions
#
# Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. Here, 0 ≤ i ≤ x; 0 ≤ j ≤ y; 0 ≤ k ≤ z. Please use list comprehensions rather than multiple loops, as a learning exercise.
#
# Example
#
# x=1
# y=1
# z=2
# n=3
#
# All permutations of [i, j, k] are:
# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]
#
# Print an array of the elements that do not sum to n=3.
#
# [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0]]
#
# Input Format
#
# Four integers x, y, z and n, each on a separate line.
#
# Constraints
#
# Print the list in lexicographic increasing order.
#
# Sample Input 0
#
 1 
 1 
 1 
 2 
#
# Sample Output 0
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
#
# Explanation 0
#
# Each variable x, y, and z will have values of 0 or 1. All permutations of lists in the form [i, j, k] = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]].
# Remove all arrays that sum to n=2 to leave only the valid permutations.
#
# Sample Input 1
#
 2 
 2 
 2 
 2 
#
# Sample Output 1
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
#
# Solution
#

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])


# 2. Basic Data Types - Find the Runner-Up Score! 
#
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
#
# Input Format
#
# The first line contains n. The second line contains an array A[] of n integers each separated by a space.
#
# Constraints
#
# 2 ≤ n ≤ 10
# -100 ≤ A[i] ≤ 100
#
# Output Format
#
# Print the runner-up score.
#
# Sample Input 0
#
 5 
 2 3 6 6 5 
#
# Sample Output 0
#
 5 
#
# Explanation 0
#
# Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
#
# Solution
#

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    maximun = max(arr)    
    second = max([i for i in arr if i != maximun])
    print(second)


# 3. Basic Data Types - Nested Lists
#
# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
#
# Example
#
# records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
# The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that score: ["beta", "alpha"]. Ordered alphabetically, the names are printed as:
#
 alpha 
 beta 
#
# Input Format
#
# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.
#
# Constraints
#
# 2 ≤ N ≤ 5
#
# There will always be one or more students having the second lowest grade.
#
# Output Format
#
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
#
# Sample Input 0
#
 5 
 Harry 
 37.21 
 Berry 
 37.21 
 Tina 
 37.2 
 Akriti 
 41 
 Harsh 
 39 
#
# Sample Output 0
#
 Berry 
 Harry 
#
# Explanation 0
#
# There are 5 students in this class whose names and grades are assembled to build the following list:
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#
# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
#
# Solution
#

if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name,score])
    
    scores.sort(key = lambda x : (x[1], x[0]))
    s = list(set(x[1] for x in scores))
    s.sort()
    s=s[1]
    for sc in scores:
        if sc[1] == s:
            print(sc[0])


# 4. Basic Data Types - Finding the percentage
#
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
#
# Example
#
# marks key: value pairs are
# 'alpha': [20, 30, 40]
# 'beta': [30, 50, 70]
# query_name = 'beta'
# The query_name is 'beta'. beta's average score is (30+50+70)/3 = 50.0.
#
# Input Format
#
# The first line contains the integer n, the number of students' records. The next n lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
#
# Constraints
#
# 2 ≤ n ≤ 10
# 0 ≤ marks[i] ≤ 100
# length of marks arrays = 3
#
# Output Format
#
# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#
# Sample Input 0
#
 3 
 Krishna 67 68 69 
 Arjun 70 98 63 
 Malika 52 56 60 
 Malika 
#
# Sample Output 0
#
 56.00 
#
# Explanation 0
#
# Marks for Malika are {52, 56, 60} whose average is (52+56+60)/3 = 56
#
# Sample Input 1
#
 2 
 Harsh 25 26.5 28 
 Anurag 26 28 30 
 Harsh 
#
# Sample Output 1
#
 26.50 
#
# Solution
#

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        mark=student_marks[query_name]
        avg=sum(mark)/len(mark)
        print('%.2f'%avg)


# 5. Basic Data Types - Lists
#
# Consider a list (list = []). You can perform the following commands:
# 1. insert i e: Insert integer e at position i.
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.
#
# Initialize your list and read in the value of n followed by lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
#
# Example
#
# N = 4
# append 1
# append 2
# insert 3 1
# print
# append 1: Append 1 to the list, arr=[1].
# append 2: Append 2 to the list, arr[1,2].
# insert 3 1: Insert 3 at index 1, arr[1,3,2].
# print: Print the array.
#
# Output:
#
 [1, 3, 2] 
#
# Input Format
#
# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.
#
# Constraints
#
# The elements added to the list must be integers.
#
# Output Format
#
# For each command of type print, print the list on a new line.
#
# Sample Input 0
#
 12 
 insert 0 5 
 insert 1 10 
 insert 0 6 
 print 
 remove 6 
 append 9 
 append 1 
 sort 
 print 
 pop 
 reverse 
 print 
#
# Sample Output 0
#
 [6, 5, 10] 
 [1, 5, 9, 10] 
 [9, 5, 1] 
#
# Solution
#

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        x = list(input().split())
        
        if(x[0] == 'insert'):
            arr.insert(int(x[1]),int(x[2]))
        elif(x[0] == 'print'):
            print(arr)
        elif(x[0] == 'remove'):
            arr.remove(int(x[1]))
        elif(x[0] == 'append'):
            arr.append(int(x[1]))
        elif(x[0] == 'sort'):
            arr.sort()
        elif(x[0] == 'pop'):
            arr.pop()
        elif(x[0] == 'reverse'):
            arr.reverse()


# 6. Basic Data Types - Tuples
#
# Task
# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
#
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported. (https://docs.python.org/3/library/functions.html#hash)
#
# Input Format
#
# The first line contains an integer, n, denoting the number of elements in the tuple.
# The second line contains n space-separated integers describing the elements in tuple t.
#
# Output Format
#
# Print the result of hash(t).
#
# Sample Input 0
#
 2 
 1 2 
#
# Sample Output 0
#
 3713081631934410656 
#
# Solution
#

if __name__ == "__main__":
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    
    print(hash(integer_list))


