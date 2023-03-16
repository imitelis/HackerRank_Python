# HackerRank - Python - Challenges - VIII - Date and Time


# 1. Date and Time - Calendar Module
#
# Calendar Module (https://docs.python.org/2/library/calendar.html#module-calendar)
#
# The calendar module allows you to output calendars and provides additional useful functions for them.
#
class calendar.TextCalendar([firstweekday]) #(https://docs.python.org/2/library/calendar.html#calendar.TextCalendar)
#
# This class can be used to generate plain text calendars.
#
# Sample Code
#
>>> import calendar
>>> 
>>> print calendar.TextCalendar(firstweekday=6).formatyear(2015)
#

                                  2015

      January                   February                   March
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
             1  2  3       1  2  3  4  5  6  7       1  2  3  4  5  6  7
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       8  9 10 11 12 13 14
11 12 13 14 15 16 17      15 16 17 18 19 20 21      15 16 17 18 19 20 21
18 19 20 21 22 23 24      22 23 24 25 26 27 28      22 23 24 25 26 27 28
25 26 27 28 29 30 31                                29 30 31

       April                      May                       June
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
          1  2  3  4                      1  2          1  2  3  4  5  6
 5  6  7  8  9 10 11       3  4  5  6  7  8  9       7  8  9 10 11 12 13
12 13 14 15 16 17 18      10 11 12 13 14 15 16      14 15 16 17 18 19 20
19 20 21 22 23 24 25      17 18 19 20 21 22 23      21 22 23 24 25 26 27
26 27 28 29 30            24 25 26 27 28 29 30      28 29 30
                          31

        July                     August                  September
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
          1  2  3  4                         1             1  2  3  4  5
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       6  7  8  9 10 11 12
12 13 14 15 16 17 18       9 10 11 12 13 14 15      13 14 15 16 17 18 19
19 20 21 22 23 24 25      16 17 18 19 20 21 22      20 21 22 23 24 25 26
26 27 28 29 30 31         23 24 25 26 27 28 29      27 28 29 30
                          30 31

      October                   November                  December
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
             1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
25 26 27 28 29 30 31      29 30                     27 28 29 30 31

#
# To learn more about different calendar functions, click here. (https://docs.python.org/2/library/calendar.html#calendar.setfirstweekday)
#
# Task
#
# You are given a date. Your task is to find what the day is on that date.
#
# Input Format
#
# A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
#
# Constraints
#
# 2000 < year < 3000
#
# Output Format
#
# Output the correct day in capital letters.
#
# Sample Input
#
 08 05 2015 
#
# Sample Output
#
 WEDNESDAY 
#
# Explanation
#
# The day on August 5th 2015 was WEDNESDAY.
#
# Solution
#

import calendar

m, d, y = map(int, input().strip().split())

print(calendar.day_name[calendar.weekday(y, m, d)].upper())


# 2. Date and Time - Time Delta
#
# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.
#
# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
#
# Day dd Mon yyyy hh:mm:ss +xxxx
#
# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
#
# Input Format
#
# The first line contains T, the number of testcases.
# Each testcase contains 2 lines, representing time t_1 and time t_2.
#
# Constraints
#
# Input contains only valid timestamps
# year ≤ 3000
#
# Output Format
#
# Print the absolute difference (t_1 - t_2) in seconds.
#
# Sample Input 0
#
 2
 Sun 10 May 2015 13:54:36 -0700 
 Sun 10 May 2015 13:54:36 -0000 
 Sat 02 May 2015 19:54:36 +0530 
 Fri 01 May 2015 13:54:36 -0000 
#
# Sample Output 0
#
 25200 
 88200 
#
# Explanation 0
#
# In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is 7 x 3600 seconds or 25200 seconds.
#
# Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 24 x 3600 + 30 x 60 => 88200
#
# Solution
#

import math
import os
import random
import re
import sys

# Complete the time_delta function below.

from datetime import datetime

def time_delta(t1, t2):
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


