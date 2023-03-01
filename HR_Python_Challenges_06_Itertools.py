# HackerRank - Python - Challenges - VI - Itertools


# 1. Itertools - itertools.product()
#
# itertools.product() (https://docs.python.org/2/library/itertools.html#itertools.product)
#
# This tool computes the cartesian product of input iterables. (https://en.wikipedia.org/wiki/Cartesian_product)
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
#
# Sample Code
#
>>> from itertools import product
>>>
>>> print list(product([1,2,3],repeat = 2))
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
>>>
>>> print list(product([1,2,3],[3,4]))
[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
>>>
>>> A = [[1,2,3],[3,4,5]]
>>> print list(product(*A))
[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
>>>
>>> B = [[1,2,3],[3,4,5],[7,8]]
>>> print list(product(*B))
[(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]
#
# Task
#
# You are given a two lists A and B. Your task is to compute their cartesian product AxB.
#
# Example
#
# A = [1, 2]
# B = [3, 4]
# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
#
# Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.
#
# Input Format
#
# The first line contains the space separated elements of list A.
# The second line contains the space separated elements of list B.
#
# Both lists have no duplicate integer elements.
#
# Constraints
#
# 0 < A < 30
# 0 < B < 30
#
# Output Format
#
# Output the space separated tuples of the cartesian product.
#
# Sample Input
#
 1 2 
 3 4 
#
# Sample Output
#
 (1, 3) (1, 4) (2, 3) (2, 4) 
#
# Solution
#

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ProdElements = list(product(A, B))
print(*ProdElements)


# 2. Itertools - itertools.permutations()
#
# itertools.permutations(iterable[, r]) (https://docs.python.org/2/library/itertools.html#itertools.permutations)
#
# This tool returns successive r length permutations of elements in an iterable.
# If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.
# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
#
# Sample Code
#
>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
#
# Task
#
# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
#
# Input Format
#
# A single line containing the space separated string S and the integer value k.
#
# Constraints
#
# 0 < k ≤ len(S)
# The string contains only UPPERCASE characters.
#
# Output Format
#
# Print the permutations of the string S on separate lines. 
#
# Sample Input
#
 HACK 2 
#
# Sample Output
#
 AC 
 AH 
 AK 
 CA 
 CH 
 CK 
 HA 
 HC 
 HK 
 KA 
 KC 
 KH 
#
# Explanation
#
# All possible size 2 permutations of the string "HACK" are printed in lexicographic sorted order.
#
# Solution
#

from itertools import permutations

S, k = list(map(str, input().split()))
fl = list(permutations(str(S), int(k)))
for i in sorted(fl):
    print("".join(i))


# 3. Itertools - itertools.combinations()
#
# itertools.combinations(iterable, r) (https://docs.python.org/2/library/itertools.html#itertools.combinations)
#
# This tool returns the r length subsequences of elements from the input iterable.
# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
#
# Sample Code
#
>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
#
# Task
#
# You are given a string S.
# Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.
#
# Input Format
#
# A single line containing the string S and integer value k separated by a space.
#
# Constraints
#
# 0 < k ≤ len(S)
#
# The string contains only UPPERCASE characters.
#
# Output Format
#
# Print the different combinations of string S on separate lines.
#
# Sample Input
#
 HACK 2 
#
# Sample Output
#
 A 
 C 
 H 
 K 
 AC 
 AH 
 AK 
 CH 
 CK 
 HK 
#
# Solution
#

from itertools import combinations

S, k = list(map(str, input().split()))
S = sorted(S)
for i in range(1,int(k)+1):
    ls = list(combinations(S,int(i))) 
    for x in ls:
        print("".join(x)) # x is a tuple


# 4. Itertools - itertools.combinations_with_replacement()
#
# itertools.combinations_with_replacement(iterable, r) (https://docs.python.org/2/library/itertools.html#itertools.combinations_with_replacement)
#
# This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
#
# Sample Code
#
>>> from itertools import combinations_with_replacement
>>> 
>>> print list(combinations_with_replacement('12345',2))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,2))
[(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]
#
# Task
#
# You are given a string S.
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.
#
# Input Format
#
# A single line containing the string S and integer value k separated by a space.
#
# Constraints
#
# 0 < k ≤ len(S)
# The string contains only UPPERCASE characters.
#
# Output Format
#
# Print the combinations with their replacements of string S on separate lines.
#
# Sample Input
#
 HACK 2 
#
# Sample Output
#
 AA 
 AC 
 AH 
 AK 
 CC 
 CH 
 CK 
 HH 
 HK 
 KK 
#
# Solution
#

from itertools import combinations_with_replacement

S,k = input().strip().split()
S = sorted(S)
ls = list(combinations_with_replacement(S,int(k))) 
for x in ls:
    print("".join(x)) # x is a tuple


# 5. Itertools - Compress the String!
#
# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools. To read more about this function, Check this out. (https://docs.python.org/2/library/itertools.html#itertools.groupby)
#
# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c) in the string.
#
# For a better understanding of the problem, check the explanation.
#
# Input Format
#
# A single line of input consisting of the string S.
#
# Output Format
#
# A single line of output consisting of the modified string.
#
# Constraints
#
# All the characters of S denote integers between 0 and 9.
# 1 ≤ |S| ≤ 10^4
#
# Sample Input
#
 1222311 
#
# Sample Output
#
 (1, 1) (3, 2) (1, 3) (2, 1) 
#
# Explanation
#
# First, the character 1 occurs only once. It is replaced by (1, 1). Then the character 2 occurs three times, and it is replaced by (3, 2) and so on.
# Also, note the single space within each compression and between the compressions. 
#
# Solution
#

import itertools

S = itertools.groupby([int(i) for i in input()])
for key,value in S:
    print(f'({len(list(value))}, {key})' , end = ' ')


# 6. Itertools - Iterables and Iterators
#
# The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.
#
# To read more about the functions in this module, check out their documentation here. (https://docs.python.org/2/library/itertools.html)
#
# You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.
# Find the probability that at least one of the K indices selected will contain the letter: 'a'.
#
# Input Format
#
# The input consists of three lines. The first line contains the integer N, denoting the length of the list. The next line consists of N space-separated lowercase English letters, denoting the elements of the list.
# The third and the last line of input contains the integer K, denoting the number of indices to be selected.
#
# Output Format
#
# Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.
#
# Note: The answer must be correct up to 3 decimal places. 
#
# Constraints
#
# 1 ≤ N ≤ 10
# 1 ≤ K ≤ N
# All the letters in the list are lowercase English letters.
#
# Sample Input
#
 4 
 a a c d 
 2 
#
# Sample Output
#
 0.8333 
#
# Explanation
#
# All possible unordered tuples of length 2 comprising of indices from 1 to 4 are:
# (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)
# Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter 'a'.
# Hence, the answer is 5/6.
#
# Solution
#

from itertools import combinations

n = int(input())
a = input().split()
k = int(input())

comb = ['a' in x for x in combinations(a, k)]
print(f'{sum(comb) / len(comb):0.3f}')


# 7. Itertools - Maximize It!
#
# You are given a function f(X) = X^2. You are also given K lists. The ith list consists of N_i elements.
#
# You have to pick one element from each list so that the value from the equation below is maximized:
#
# S = (f(X_1) + f(X_2) + ... + f(X_k))%M
#
# X_i denotes the element picked from the list ith. Find the maximized value S_max obtained.
# % denotes the modulo operator.
#
# Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.
#
# Input Format
#
# The first line contains 2 space separated integers K and M.
# The next K lines each contains an integer N_i, denoting the number of elements in the ith list, followed by N_i space separated integers denoting the elements in the list.
#
# Constraints
#
# 1 ≤ K ≤ 7
# 1 ≤ M ≤ 1000
# 1 ≤ N_i ≤ 7
# 1 ≤ Magnitude of elements in list ≤ 10^9
#
# Output Format
#
# Output a single integer denoting the value S_max.
#
# Sample Input
#
 3 1000 
 2 5 4 
 3 7 8 9 
 5 5 7 8 9 10 
#
# Sample Output
#
 206 
#
# Explanation
#
# Picking 5 from the 1st list, 9 from the 2nd list 10 and from the 3rd list gives the maximum S value equal to (5^2 + 9^2 + 10^2)%1000 = 206.
#
# Solution
#

from itertools import product

K, M = map(int,input().split())
ls = []
for _ in range(K):
    ls.append(list(map(int,input().split()))[1:])

ls_S = []
for elem in product(*ls):
    ls_S.append(sum([x*x for x in elem])%M)
print(max(ls_S))


