# HackerRank - Python - Challenges - X - Classes


# 1. Classes - Classes: Dealing with Complex Numbers
#
# For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.
#
# The real and imaginary precision part should be correct up to two decimal places.
#
# Input Format
#
# One line of input: The real and imaginary part of a number separated by a space.
#
# Output Format
#
# For two complex numbers C and D, the output should be in the following sequence on separate lines:
# C+D
# C-D
# C*D
# C/D
# mod(C)
# mod(D)
#
# For complex numbers with non-zero real (A) and complex part (B), the output should be in the following format:
# A+Bi
# Replace the plus symbol (+) with a minus symbol (-) when B<0.
#
# For complex numbers with a zero complex part i.e. real numbers, the output should be:
# A+0.00i
#
# For complex numbers where the real part is zero and the complex part is non-zero, the output should be:
# 0.00+Bi
#
# Sample Input
#
 2 1 
 5 6 
#
# Sample Output
#
 7.00+7.00i 
 -3.00-5.00i 
 4.00+17.00i 
 0.26-0.11i 
 2.24+0.00i 
 7.81+0.00i 
#
# Concept
#
# Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer here. (https://diveintopython3.net/iterators.html#defining-classes)
#
# Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality.
#

__add__-> Can be overloaded for + operation

__sub__ -> Can be overloaded for - operation

__mul__ -> Can be overloaded for * operation

#
# For more information on operator overloading in Python, refer here. (https://docs.python.org/3.2/reference/datamodel.html)
#
# Solution
#

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real,self.imaginary + no.imaginary )
    def __sub__(self, no):
        return Complex(self.real - no.real,self.imaginary - no.imaginary )
    def __mul__(self, no):
        return Complex((self.real * no.real)-(self.imaginary * no.imaginary),                                   (self.real*no.imaginary)+(self.imaginary * no.real))
    def __truediv__(self, no):
        z=(complex(self.real,self.imaginary)/complex(no.real,no.imaginary))
        return Complex(z.real,z.imag)
    def mod(self):
        return Complex(abs(complex(self.real,self.imaginary)),0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


# 2. Classes - Class 2 - Find the Torsional Angle
#
# You are given four points A, B, C and D in a 3-dimensional Cartesian coordinate system. You are required to print the angle between the plane made by the points A, B, C and B, C, D in degrees(not radians). Let the angle be PHI.
# Cos(PHI) = (X.Y)/|X||Y| where X=ABxBC and Y=BCxCD.
# Here, X.Y means the dot product of X and Y, and ABxCD means the cross product of vectors AB and BC. Also, AB=B-A.
#
# Input Format
# 
# One line of input containing the space separated floating number values of the X, Y and Z coordinates of a point.
#
# Output Format
#
# Output the angle correct up to two decimal places.
#
# Sample Input
#
 0 4 5 
 1 7 6 
 0 5 9 
 1 7 2 
#
# Sample Output
#
 8.19 
#
# Solution
#

import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, no):
        return __class__((self.x-no.x),(self.y-no.y),(self.z-no.z))

    def dot(self, no):
        return ((self.x*no.x)+(self.y*no.y)+(self.z*no.z))
    
    def cross(self, no):
        x=(self.y*no.z)-(self.z*no.y)
        y=(self.x*no.z)-(self.z*no.x)
        z = (self.x*no.y)-(self.y*no.x)
        return __class__(x,y,z)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))


