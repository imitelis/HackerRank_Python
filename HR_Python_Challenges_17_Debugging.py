# HackerRank - Python - Challenges - XVII - Debugging


# 1. Debugging - Words Score
#
# In this challenge, the task is to debug the existing code to successfully execute all provided test files.
#
# Consider that vowels in the alphabet are a, e, i, o, u and y.
#
# Function score_words takes a list of lowercase words as an argument and returns a score as follows:
#
# The score of a single word is 2 if the word contains an even number of vowels. # Otherwise, the score of this word is 1. The score for the whole list of words is the sum of scores of all words in the list.
#
# Debug the given function score_words such that it returns a correct score.
#
# Your function will be tested on several cases by the locked template code.
#
# Input Format
#
# The input is read by the provided locked code template. In the first line, there is a single integer n denoting the number of words. In the second line, there are space-separated lowercase words.
#
# Constraints
#
# 1 ≤ n ≤ 20
#
# - Each word has at most 20 letters and all letters are English lowercase letters
#
# Output Format
#
# The output is produced by the provided and locked code template. It calls function score_words with the list of words read from the input as the argument and prints the returned score to the output.
#
# Sample Input 0
#
 2 
 hacker book 
#
# Sample Output 0
#
 4 
#
# Explanation 0
#
# There are two words in the input: hacker and book. The score of the word hacker is 2 because it contains an even number of vowels, i.e. 2 vowels, and the score of book is 2 for the same reason. Thus the total score is 2+2=4.
#
# Sample Input 1
#
 3 
 programming is awesome 
#
# Sample Output 1
#
 4 
#
# Explanation 1
#
# There are 3 words in the input: programming, is and awesome. The score of programming is 1 since it contains 3 vowels, an odd number of vowels. The score of is is also 1 because it has an odd number of vowels. The score of awesome is 2 since it contains 4 vowels, an even number of vowels. Thus, the total score is 1+1+2=4.
#
# Solution
#

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))


# 2. Debugging - Default Arguments
#
# In this challenge, the task is to debug the existing code to successfully execute all provided test files.
#
# Python supports a useful concept of default argument values. For each keyword argument of a function, we can assign a default value which is going to be used as the value of said argument if the function is called without it. For example, consider the following increment function:
#
def increment_by(n, increment=1):
    return n + increment
#
# The functions works like this:
#
>>> increment_by(5, 2)
7
>>> increment_by(4)
5
>>>
#
# Debug the given function print_from_stream using the default value of one of its arguments.
#
# The function has the following signature:
#
def print_from_stream(n, stream)
#
# This function should print the first n values returned by get_next() method of stream object provided as an argument. Each of these values should be printed in a separate line.
#
# Whenever the function is called without the stream argument, it should use an instance of EvenStream class defined in the code stubs below as the value of stream.
#
# Your function will be tested on several cases by the locked template code.
#
# Input Format
#
# The input is read by the provided locked code template. In the first line, there is a single integer q denoting the number of queries. Each of the following q lines contains a stream_name followed by integer n, and it corresponds to a single test for your function.
#
# Constraints
#
# 1 ≤ q ≤ 100
# 1 ≤ n ≤ 10
#
# Output Format
#
# The output is produced by the provided and locked code template. For each of the queries (stream_name, n), if the stream_name is even then print_from_stream(n) is called. Otherwise, if the stream_name is odd, then print_from_stream(n, OddStream()) is called.
#
# Sample Input 0
#
 3 
 odd 2 
 even 3 
 odd 5 
#
# Sample Output 0
#
 1 
 3 
 0 
 2 
 4 
 1 
 3 
 5 
 7 
 9 
#
# Explanation 0
#
# There are 3 queries in the sample.
#
# In the first query, the function print_from_stream(2, OddStream()) is exectuted, which leads to printing values 1 and 3 in separated lines as the first two non-negative odd numbers.
#
# In the second query, the function print_from_stream(3) is exectuted, which leads to printing values 2,4 and 6 in separated lines as the first three non-negative even numbers.
#
# In the third query, the function print_from_stream(5, OddStream()) is exectuted, which leads to printing values 1,3,5,7 and 9 in separated lines as the first five non-negative odd numbers.
#
# Solution
#

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())
    stream.__init__()


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())


