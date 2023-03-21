# HackerRank - Python - Challenges - XIII - Regex and Parsing


# 1. Regex and Parsing - Detect Floating Point Number
#
# Check Tutorial tab to know how to to solve. (https://www.hackerrank.com/challenges/introduction-to-regex/tutorial)
#
# You are given a string N.
# Your task is to verify that N is a floating point number.
#
# In this task, a valid float number must satisfy all of the following requirements:
#
# Number can start with +, - or . symbol.
# For example:
# ✔+4.50
# ✔-1.0
# ✔.5
# ✔-.7
# ✔+.4
# ✖ -+4.5
#
# Number must contain at least 1 decimal value.
# For example:
# ✖ 12.
# ✔12.0  
#
# Number must have exactly one . symbol.
# Number must not give any exceptions when converted using float(N).
#
# Input Format
#
# The first line contains an integer T, the number of test cases.
# The next T line(s) contains a string N.
#
# Constraints
#
# 0 < T < 10
#
# Output Format
#
# Output True or False for each test case.
#
# Sample Input 0
#
 4 
 4.0O0 
 -1.00 
 +4.54 
 SomeRandomStuff 
#
# Sample Output 0
#
 False 
 True 
 True 
 False 
#
# Explanation 0
#
# 4.0O0: O is not a digit.
# -1.00: is valid.
# +4.54: is valid.
# SomeRandomStuff: is not a number.
#
# Solution
#

import re

regex = r'^[-+]?\d*[.]\d+$';
T = int(input())

for i in range(T):
    txt= input()
    if re.search(regex,txt): print(True)
    else: print(False)


# 2. Regex and Parsing - Re.split()
#
# Check Tutorial tab to know how to to solve. (https://www.hackerrank.com/challenges/re-split/tutorial)
#
# You are given a string s consisting only of digits 0-9, commas ,, and dots .
#
# Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in s.
#
# It’s guaranteed that every comma and every dot in s is preceeded and followed by a digit.
#
# Sample Input 0
#
 100,000,000.000 
#
# Sample Output 0
#
 100 
 000 
 000 
 000 
#
# Solution
#

regex_pattern = r"[\,\.]" #Do not delete 'r'.

import re

print("\n".join(re.split(regex_pattern, input())))


# 3. Regex and Parsing - Group(), Groups() & Groupdict()
#
# group() (https://docs.python.org/2/library/re.html#re.MatchObject.group)
#
# A group() expression returns one or more subgroups of the match.
#
# Code
#
>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.group(0)       # The entire match 
'username@hackerrank.com'
>>> m.group(1)       # The first parenthesized subgroup.
'username'
>>> m.group(2)       # The second parenthesized subgroup.
'hackerrank'
>>> m.group(3)       # The third parenthesized subgroup.
'com'
>>> m.group(1,2,3)   # Multiple arguments give us a tuple.
('username', 'hackerrank', 'com')
#
# groups() (https://docs.python.org/2/library/re.html#re.MatchObject.groups)
#
# A groups() expression returns a tuple containing all the subgroups of the match.
#
# Code
#
>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.groups()
('username', 'hackerrank', 'com')
#
# groupdict() (https://docs.python.org/2/library/re.html#re.MatchObject.groupdict)
#
# A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
#
# Code
#
>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
#
# Task
#
# You are given a string S.
# Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.
#
# Input Format
#
# A single line of input containing the string S.
#
# Constraints
#
# 0 < len(S) < 100
#
# Output Format
#
# Print the first occurrence of the repeating character. If there are no repeating characters, print -1.
#
# Sample Input
#
 ..12345678910111213141516171820212223 
#
# Sample Output
#
 1 
#
# Explanation
#
# .. is the first repeating character, but it is not alphanumeric.
# 1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.
#
# Solution
#

import re

m = re.search(r"([a-z0-9])\1{1,}", input())

if m:
    print(m.group(1))
else:
    print(-1)


# 4. Regex and Parsing - Re.findall() & Re.finditer()
#
# re.findall() (https://docs.python.org/2/library/re.html#re.findall)
#
# The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.
#
# Code
#
>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
#
# re.finditer() (https://docs.python.org/2/library/re.html#re.finditer)
#
# The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
#
# Code
#
>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
#
# Task
#
# You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of S that contains or more vowels.
# Also, these substrings must lie in between 2 consonants and should contain vowels only.
#
# Note :
#
# Vowels are defined as: AEIOU and aeiou.
# Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.
#
# Input Format
#
# A single line of input containing string S.
#
# Constraints
#
# 0 < len(S) < 100
#
# Output Format
#
# Print the matched substrings in their order of occurrence on separate lines.
# If no match is found, print -1.
#
# Sample Input
#
 rabcdeefgyYhFjkIoomnpOeorteeeeet 
#
# Sample Output
#
 ee 
 Ioo 
 Oeo 
 eeeee 
#
# Explanation
#
# ee is located between consonant d and f.
# Ioo is located between consonant k and m.
# Oeo is located between consonant p and r.
# eeeee is located between consonant t and t. 
#
# Solution
#

import re

pat = "(?<=[^aeiou])([aeiou]{2,})[^aeiou]"
res = re.findall(pat, input(), flags=re.I)

print('\n'.join(res or ['-1']))


# 5. Regex and Parsing - Re.start() & Re.end()
#
# start() & end() (https://docs.python.org/2/library/re.html#re.MatchObject.start)
#
# These expressions return the indices of the start and end of the substring matched by the group.
#
# Code
#
>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0
#
# Task
#
# You are given a string S.
# Your task is to find the indices of the start and end of string k in S.
#
# Input Format
#
# The first line contains the string.
# The second line contains the string.
#
# Constraints
#
# 0 < len(S) < 100
# 0 < len(k) < len(S)
# Output Format
#
# Print the tuple in this format: (start _index, end _index).
# If no match is found, print (-1, -1).
#
# Sample Input
#
 aaadaa 
 aa 
#
# Sample Output
#
 (0, 1) 
 (1, 2) 
 (4, 5) 
#
# Solution
#

import re

S, k = input(), input()
pattern = r'{}'.format('{}(?={})'.format(k[0:-1], k[-1]))
r = re.finditer(pattern, S)
b = True    

for m in r:
    b = False
    print((m.start(), m.end()))
if b:
    print((-1, -1))


# 6. Regex and Parsing - Regex Substitution
#
# The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
# The method is called for all matches and can be used to modify strings in different ways.
# The re.sub() method returns the modified string as an output.
#
# Learn more about re.sub(). (https://docs.python.org/3/library/re.html)
#
# Transformation of Strings
#
# Code
#
import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
#
# Output
#
 1 4 9 16 25 36 49 64 81 
#
#
# Replacements in Strings
#
# Code
#
import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

print re.sub("(<!--.*?-->)", "", html) #remove comment
#
# Output
#
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">

  <param name="quality" value="high"/>
</object>
#
# Task
#
# You are given a text of N lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:
# && → and
# || → or
#
# Both && and || should have a space " " on both sides.
#
# Input Format
#
# The first line contains the integer, N.
# The next N lines each contain a line of the text.
#
# Constraints
#
# 0 < N < 100
# Neither && nor || occur in the start or end of each line.
#
# Output Format
#
# Output the modified text.
#
# Sample Input
#
 11 
 a = 1; 
 b = input(); 
 
 if a + b > 0 && a - b < 0: 
     start() 
 elif a*b > 10 || a/b < 1: 
     stop() 
 print set(list(a)) | set(list(b)) 
 #Note do not change &&& or ||| or & or | 
 #Only change those '&&' which have space on both sides. 
 #Only change those '|| which have space on both sides. 
#
# Sample Output
#
 a = 1; 
 b = input(); 
 
 if a + b > 0 and a - b < 0: 
     start() 
 elif a*b > 10 or a/b < 1: 
     stop() 
 print set(list(a)) | set(list(b)) 
 #Note do not change &&& or ||| or & or | 
 #Only change those '&&' which have space on both sides. 
 #Only change those '|| which have space on both sides. 
#
# Solution
#

import re

N = int(input())

for _ in range(N):
    line = input()
    line = re.sub(r'(?<= )\&{2}(?= )', 'and', line)
    line = re.sub(r'(?<= )\|{2}(?= )', 'or', line)
    print(line)


# 7. Regex and Parsing - Validating Roman Numerals
#
# You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.
#
# Input Format
#
# A single line of input containing a string of Roman characters.
#
# Output Format
#
# Output a single line containing True or False according to the instructions above.
#
# Constraints
#
# The number will be between 1 and 3999 (both included).
#
# Sample Input
#
 CDXXI 
#
# Sample Output
#
 True 
#
# References
#
# Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python. (https://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-13--regular-expression-matching)
#
# (https://developers.google.com/edu/python/regular-expressions) 
#
# Solution
#

regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$" # Do not delete 'r'.

import re

print(str(bool(re.match(regex_pattern, input()))))


# 8. Regex and Parsing - Validating phone numbers
#
# Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
#
# A valid mobile number is a ten digit number starting with a 7, 8 or 9.
#
# Concept
#
# A valid mobile number is a ten digit number starting with a 7, 8 or 9.
#
# Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python. (https://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-13--regular-expression-matching)
#
# (https://developers.google.com/edu/python/regular-expressions)
#
# Input Format
#
# The first line contains an integer N, the number of inputs.
# N lines follow, each containing some string.
#
# Constraints
#
# 1 ≤ N ≤ 10
# 2 ≤ len(Number) ≤ 15
#
# Output Format
#
# For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.
#
# Sample Input
#
 2 
 9587456281 
 1252478965 
#
# Sample Output
#
 YES 
 NO 
#
# Solution
#

import re

N = int(input())

for _ in range(N):
    if re.match(r'^(7|8|9)\d{9}$', input()):
        print('YES')
    else: print('NO')


# 9. Regex and Parsing - Validating and Parsing Email Addresses
#
# A valid email address meets the following criteria:
#  1.  It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
#  2.  The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _. ()
#  3.  The domain and extension contain only English alphabetical characters. (https://en.wikipedia.org/wiki/English_alphabet)
#  4.  The extension is 1, 2, or 3 characters in length.
#
# Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.
#
# Hint: Try using Email.utils() to complete this challenge. For example, this code:
#
import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))
#
# produces this output:
#
 ('DOSHI', 'DOSHI@hackerrank.com') 
 DOSHI <DOSHI@hackerrank.com> 
#
# (https://docs.python.org/3/library/email.utils.html)
#
# Input Format
#
# The first line contains a single integer, n, denoting the number of email address.
# Each line i of the n subsequent lines contains a name and an email address as two space-separated values following this format:
#
# name <user@email.com>
#
# Constraints
#
# 0 < n < 100
#
# Output Format
#
# Print the space-separated name and email address pairs containing valid email addresses only. Each pair must be printed on a new line in the following format:
#
# name <user@email.com>
#
# You must print each valid email address in the same order as it was received as input.
#
# Sample Input
#
 2 
 DEXTER <dexter@hotmail.com> 
 VIRUS <virus!@variable.:p> 
#
# Sample Output
#
 DEXTER <dexter@hotmail.com> 
#
# Explanation
#
# dexter@hotmail.com is a valid email address, so we print the name and email address pair received as input on a new line.
# virus!@variable.:p is not a valid email address because the username contains an exclamation point (!) and the extension contains a colon (:). As this email is not valid, we print nothing.
#
# Solution
#

import re

for _ in range(int(input())):
    user, email = input().split()
    if re.match(r'^[a-zA-Z]+[\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email[1:-1]):
        print(f'{user} {email}')


# 10. Regex and Parsing - Hex Color Code
#
# CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
#
# Specifications of HEX Color Code
#
#  ■  It must start with a '#' symbol.
#  ■  It can have 3 or 6 digits.
#  ■  Each digit is in the range of 0 to F. (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E and F).
#  ■  A - F letters can be lower case. (a, b, c, d, e and f are also valid digits).
#
# Examples
#
# Valid Hex Color Codes
# #FFF
# #025
# #F0A1FB
#
# Invalid Hex Color Codes
# #fffabg
# #abcf
# #12365erff
#
# You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.
#
# CSS Code Pattern
#
Selector
{
	Property: Value;
}
#
# Input Format
#
# The first line contains N, the number of code lines.
# The next N lines contains CSS Codes.
#
# Constraints
#
# 0 < N < 50
#
# Output Format
#
# Output the color codes with '#' symbols on separate lines.
#
# Sample Input
#
 11 
 #BED 
 { 
     color: #FfFdF8; background-color:#aef; 
     font-size: 123px; 
     background: -webkit-linear-gradient(top, #f9f9f9, #fff); 
 } 
 #Cab 
 { 
     background-color: #ABC; 
     border: 2px dashed #fff; 
 } 
#
# Sample Output
#
 #FfFdF8 
 #aef 
 #f9f9f9 
 #fff 
 #ABC 
 #fff 
#
# Explanation
#
# #BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.
#
# Hence, the valid color codes are:
# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff
#
# Note: There are no comments ( // or /* */) in CSS Code.
#
# Solution
#

import re

for _ in range(int(input())):
    for i in re.findall(r'(?<=[ :,])#[0-9A-Fa-f]{3,6}', input()):
        print(i)


# 11. Regex and Parsing - HTML Parser - Part 1
#
# HTML (https://es.wikipedia.org/wiki/HTML)
#
# Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.
#
# Parsing (https://en.wikipedia.org/wiki/Parsing)
#
# Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string into its component parts and describing their syntactic roles.
#
# HTMLParser (https://docs.python.org/2/library/htmlparser.html#HTMLParser.HTMLParser)
#
# An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered.
#
# Example (based on the original Python documentation):
#
# Code
#
from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Found a start tag  :", tag
    def handle_endtag(self, tag):
        print "Found an end tag   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Found an empty tag :", tag

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed("<html><head><title>HTML Parser - I</title></head>"
            +"<body><h1>HackerRank</h1><br /></body></html>")
#
# Output
#
 Found a start tag  : html 
 Found a start tag  : head 
 Found a start tag  : title 
 Found an end tag   : title 
 Found an end tag   : head 
 Found a start tag  : body 
 Found a start tag  : h1 
 Found an end tag   : h1 
 Found an empty tag : br 
 Found an end tag   : body 
 Found an end tag   : html 
#
# .handle_starttag(tag, attrs) (https://docs.python.org/2/library/htmlparser.html#HTMLParser.HTMLParser.handle_starttag)
#
# This method is called to handle the start tag of an element. (For example: <div class='marks'>)
# The tag argument is the name of the tag converted to lowercase.
# The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag’s <> brackets.
#
# .handle_endtag(tag) (https://docs.python.org/2/library/htmlparser.html#HTMLParser.HTMLParser.handle_endtag)
#
# This method is called to handle the end tag of an element. (For example: </div>)
# The tag argument is the name of the tag converted to lowercase.
#
# .handle_startendtag(tag,attrs) (https://docs.python.org/2/library/htmlparser.html#HTMLParser.HTMLParser.handle_startendtag)
#
# This method is called to handle the empty tag of an element. (For example: <br />)
# The tag argument is the name of the tag converted to lowercase.
# The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag’s <> brackets.
#
# Task
#
# You are given an HTML code snippet of N lines.
# Your task is to print start tags, end tags and empty tags separately.
#
# Format your results in the following way:
#
 Start : Tag1 
 End   : Tag1 
 Start : Tag2 
 -> Attribute2[0] > Attribute_value2[0] 
 -> Attribute2[1] > Attribute_value2[1] 
 -> Attribute2[2] > Attribute_value2[2] 
 Start : Tag3 
 -> Attribute3[0] > None 
 Empty : Tag4 
 -> Attribute4[0] > Attribute_value4[0] 
 End   : Tag3 
 End   : Tag2 
#
# Here, the -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
# The > symbol acts as a separator of the attribute and the attribute value.
#
# If an HTML tag has no attribute then simply print the name of the tag.
# If an attribute has no attribute value then simply print the name of the attribute value as None.
#
# Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->).Comments can be multiline as well.
#
# Input Format
#
# The first line contains integer N, the number of lines in a HTML code snippet.
# The next N lines contain HTML code.
#
# Constraints
#
# 0 < N < 100
#
# Output Format
#
# Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.
#
# Use proper formatting as explained in the problem statement.
#
# Sample Input
#
 2 
 <html><head><title>HTML Parser - I</title></head> 
 <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html> 
#
# Sample Output
#
 Start : html 
 Start : head 
 Start : title 
 End   : title 
 End   : head 
 Start : body 
 -> data-modal-target > None 
 -> class > 1 
 Start : h1 
 End   : h1 
 Empty : br 
 End   : body 
 End   : html 
#
# Solution
#

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")

parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())


# 12. Regex and Parsing - HTML Parser - Part 2
#
# *This section assumes that you understand the basics discussed in HTML Parser - Part 1
#
# .handle_comment(data) (https://docs.python.org/2/library/htmlparser.html#HTMLParser.HTMLParser.handle_comment)
#
# This method is called when a comment is encountered (e.g. <!--comment-->).
# The data argument is the content inside the comment tag:
#
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
          print "Comment  :", data
#
# .handle_data(data) (https://docs.python.org/2/library/htmlparser.html#HTMLParser.HTMLParser.handle_data)
#
# This method is called to process arbitrary data (e.g. text nodes and the content of <script>...</script> and <style>...</style>).
# The data argument is the text content of HTML.
#
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        print "Data     :", data
#
# Task
#
# You are given an HTML code snippet of N lines.
# Your task is to print the single-line comments, multi-line comments and the data.
#
# Print the result in the following format:
#
 >>> Single-line Comment 
 Comment 
 >>> Data 
 My Data 
 >>> Multi-line Comment 
 Comment_multiline[0] 
 Comment_multiline[1] 
 >>> Data 
 My Data 
 >>> Single-line Comment: 
#
# Note: Do not print data if data == '\n'.
#
# Input Format
#
# The first line contains integer N, the number of lines in the HTML code snippet.
# The next N lines contains HTML code.
#
# Constraints
#
# 0 < N < 100
#
# Output Format
#
# Print the single-line comments, multi-line comments and the data in order of their occurrence from top to bottom in the snippet.
#
# Format the answers as explained in the problem statement.
#
# Sample Input
#
 4 
 <!--[if IE 9]>IE9-specific content 
 <![endif]--> 
 <div> Welcome to HackerRank</div> 
 <!--[if IE 9]>IE9-specific content<![endif]--> 
#
# Sample Output
#
 >>> Multi-line Comment 
 [if IE 9]>IE9-specific content 
 <![endif] 
 >>> Data 
 Welcome to HackerRank 
 >>> Single-line Comment 
 [if IE 9]>IE9-specific content<![endif] 
#
# Solution
#

from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
  
    def handle_comment(self, data):
        if re.search(r'\n', data):
            print('>>> Multi-line Comment')
            print(data)
        else:
            print('>>> Single-line Comment')
            print(data)

    def handle_data(self, data):
        if data!='\n':
            print(">>> Data")
            print(data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# 13. Regex and Parsing - Detect HTML Tags, Attributes and Attribute Values
#
# You are given an HTML code snippet of N lines.
# Your task is to detect and print all the HTML tags, attributes and attribute values.
#
# Print the detected items in the following format:
#
 Tag1 
 Tag2 
 -> Attribute2[0] > Attribute_value2[0] 
 -> Attribute2[1] > Attribute_value2[1] 
 -> Attribute2[2] > Attribute_value2[2] 
 Tag3 
 -> Attribute3[0] > Attribute_value3[0] 
#
# The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
# The > symbol acts as a separator of attributes and attribute values.
#
# If an HTML tag has no attribute then simply print the name of the tag.
#
# Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be multiline.
# All attributes have an attribute value.
#
# Input Format
#
# The first line contains an integer N, the number of lines in the HTML code snippet.
# The next N lines contain HTML code.
#
# Constraints
#
# 0 < N < 100
#
# Output Format
#
# Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet.
#
# Format your answers as explained in the problem statement.
#
# Sample Input
#
 9 
 <head> 
 <title>HTML</title> 
 </head> 
 <object type="application/x-flash" 
   data="your-file.swf" 
   width="0" height="0"> 
   <!-- <param name="movie" value="your-file.swf" /> --> 
   <param name="quality" value="high"/> 
 </object> 
#
# Sample Output
#
 head 
 title 
 object 
 -> type > application/x-flash 
 -> data > your-file.swf 
 -> width > 0 
 -> height > 0 
 param 
 -> name > quality 
 -> value > high 
#
# Explanation
#
#  1.  head tag: Print the head tag only because it has no attribute.
#  2.  title tag: Print the title tag only because it has no attribute.
#  3.  object tag: Print the object tag. In the next 4 lines, print the attributes type, data, width and height along with their respective values.
#  4.  <!-- Comment --> tag: Don't detect anything inside it.
#  5.  param tag: Print the param tag. In the next 2 lines, print the attributes name along with their respective values.
#
# Solution
#

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print(tag)
        for i in attr:
            print(f'-> {i[0]} > {i[1]}')
   
html=""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
                
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# 14. Regex and Parsing - Validating UID
#
# ABCXYZ company has up to 100 employees.
# The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.
#
# A valid UID must follow the rules below:
#  1.  It must contain at least 2 uppercase English alphabet characters.
#  2.  It must contain at least 3 digits (0 - 9).
#  3.  It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
#  4.  No character should repeat.
#  5.  There must be exactly 10 characters in a valid UID.
#
# Input Format
#
# The first line contains an integer T, the number of test cases.
# The next T lines contains an employee's UID.
#
# Output Format
#
# For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.
#
# Sample Input
#
 2 
 B1CD102354 
 B1CDEF2354 
#
# Sample Output
#
 Invalid 
 Valid 
#
# Explanation
#
# B1CD102354: 1 is repeating → Invalid
# B1CDEF2354: Valid
#
# Solution
#

import re

pattern = r'(?!.*(.).*\1)(?=.*\d.*\d.*\d)(?=.*[A-Z].*[A-Z])[A-Za-z0-9]{10}'

for _ in range(int(input())):
    if re.match(pattern, input()):
        print('Valid')    
    else:  
        print('Invalid')


# 15. Regex and Parsing - Validating Credit Card Numbers
#
# You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!
#
# A valid credit card from ABCD Bank has the following characteristics:
#
#  ►  It must start with a 4, 5 or 6.
#  ►  It must contain exactly 16 digits.
#  ►  It must only consist of digits (0 - 9).
#  ►  It may have digits in groups of 4, separated by one hyphen "-".
#  ►  It must NOT use any other separator like ' ' , '_', etc.
#  ►  It must NOT have 4 or more consecutive repeated digits.
#
# Examples:
#
# Valid Credit Card Numbers
#
# 4253625879615786
# 4424424424442444
# 5122-2368-7954-3214
#
# Invalid Credit Card Numbers
#
# 42536258796157867       #17 digits in card number → Invalid 
# 4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
# 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
# 44244x4424442444        #Contains non digit characters → Invalid
# 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
#
# Input Format
#
# The first line of input contains an integer N.
# The next N lines contain credit card numbers.
#
# Constraints
#
# 0 < N < 100
#
# Output Format
#
# Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.
#
# Sample Input
#
 6
 4123456789123456 
 5123-4567-8912-3456 
 61234-567-8912-3456 
 4123356789123456 
 5133-3367-8912-3456 
 5123 - 3567 - 8912 - 3456 
#
# Sample Output
#
 Valid 
 Valid 
 Invalid 
 Valid 
 Invalid 
 Invalid 
#
# Explanation
#
# 4123456789123456 : Valid
# 5123-4567-8912-3456 : Valid
# 61234-567-8912-3456 : Invalid, because the card number is not divided into equal groups of 4.
# 4123356789123456 : Valid
# 51-67-8912-3456 : Invalid, consecutive digits 3333 is repeating 4 times.
# 5123 - 4567 - 8912 - 3456 : Invalid, because space ' ' and - are used as separators.
#
# Solution
#

import re

pattern = r'(?!.*(\d)(-?\1){3}.*)^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$'

for _ in range(int(input())):
    if re.match(pattern, input()):
        print('Valid')
    else:
        print('Invalid')


# 16. Regex and Parsing - Validating Postal Codes
#
# A valid postal code P have to fullfil both below requirements:
#  1.  P must be a number in the range from 100000 to 999999 inclusive.
#  2.  P must not contain more than one alternating repetitive digit pair.
#
# Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
#
# For example:
#
# 121426 # Here, 1 is an alternating repetitive digit.
# 523563 # Here, NO digit is an alternating repetitive digit.
# 552523 # Here, both 2 and 5 are alternating repetitive digits.
#
# Your task is to provide two regular expressions regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:
#
# regex_integer_in_range should match only integers range from 100000 to 999999 inclusive
#
# regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.
#
# Both these regular expressions will be used by the provided code template to check if the input string P is a valid postal code using the following expression:
#
(bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
#
# Input Format
#
# Locked stub code in the editor reads a single string denoting P from stdin and uses provided expression and your regular expressions to validate if P is a valid postal code.

# Output Format
#
# You are not responsible for printing anything to stdout. Locked stub code in the editor does that.
#
# Sample Input 0
#
 110000 
#
# Sample Output 0
#
 False 
#
# Explanation 0
#
# 1 1 0000 : (0, 0) and (0, 0) are two alternating digit pairs. Hence, it is an invalid postal code.
#
# Note:
# A score of 0 will be awarded for using 'if' conditions in your code.
# You have to pass all the testcases to get a positive score.
#
# Solution
#

regex_integer_in_range = r"^[1-9]{1}[0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# 17. Regex and Parsing - Matrix Script
#
# Neo has a complex matrix script. The matrix script is a NxM grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
#
# [/data/Matrix_Script.jpg]
#
# (https://s3.amazonaws.com/hr-challenge-images/12524/1442753362-1075bd12d9-Capture.JPG)
#
# To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.
#
# If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.
#
# Neo feels that there is no need to use 'if' conditions for decoding.
#
# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
#
# Input Format
#
# The first line contains space-separated integers N (rows) and M (columns) respectively.
# The next N lines contain the row elements of the matrix script.
#
# Constraints
#
# 0 < N, M < 100
# Note: A 0 score will be awarded for using 'if' conditions in your code.
#
# Output Format
#
# Print the decoded matrix script.
#
# Sample Input 0
#
 7 3 
 Tsi 
 h%x 
 i # 
 sM 
 $a 
 #t% 
 ir! 
#
# Sample Output 0
#
 This is Matrix#  %! 
#
# Explanation 0
#
# The decoded script is:
#
 This$#is% Matrix#  %! 
#
# Neo replaces the symbols or spaces between two alphanumeric characters with a single space   ' ' for better readability.
#
# So, the final decoded script is:
#
 This is Matrix#  %! 
#
# Solution
#

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

text = ''
for j in range(m):
    for row in matrix:
        text += row[j]

print(''.join(re.sub(r'(?<=[A-Za-z0-9])[\W_]+(?=[A-Za-z0-9])', ' ', text)))

