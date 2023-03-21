# HackerRank - Python - Challenges - XIV - XML


# 1. XML - XML 1 - Find the Score
#
# You are given a valid XML document, and you have to print its score. The score is calculated by the sum of the score of each element. For any element, the score is equal to the number of attributes it has.
#
# Input Format
#
# The first line contains N, the number of lines in the XML document.
# The next N lines follow containing the XML document.
#
# Output Format
#
# Output a single line, the integer score of the given XML document.
#
# Sample Input 
#
 6 
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
#
# Sample Output
#
 5 
#
# Explanation
#
# The feed and subtitle tag have one attribute each - lang.
# The title and updated tags have no attributes.
# The link tag has three attributes - rel, type and href.
# So, the total score is 1+1+3=5.
#
# There may be any level of nesting in the XML document. To learn about XML parsing, refer here. (https://diveintopython3.net/xml.html)
#
# NOTE: In order to parse and generate an XML element tree, use the following code:
#
>> import xml.etree.ElementTree as etree
>> tree = etree.ElementTree(etree.fromstring(xml))
#
# Here, XML is the variable containing the string.
# Also, to find the number of keys in a dictionary, use the len function:
#
>> dicti = {'0': 'This is zero', '1': 'This is one'}
>> print (len(dicti))

2
#
# Solution
#

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    if len(node) == 0:
        return len(node.attrib)
    else:
        return len(node.attrib) + sum([get_attr_number(child) for child in node])

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# 2. XML - XML 2 - Find the Maximum Depth
#
# You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as 0.
#
# Input Format
#
# The first line contains N, the number of lines in the XML document.
# The next N lines follow containing the XML document.
#
# Output Format
#
# Output a single line, the integer value of the maximum level of nesting in the XML document.
#
# Sample Input
#
 6 
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>
#
# Sample Output
#
 1 
#
# Explanation
#
# Here, the root is a feed tag, which has depth of 0.
# The tags title, subtitle, link and updated all have a depth of 1.
#
# Thus, the maximum depth is 1.
#
# Solution
#

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    maxdepth = max(maxdepth, level + 1)
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


