#Numbers
'''
Python supports Booleans, integers, floating point numbers, and complex numbers. 
They are defined as bool, int, float, and complex class in Python. 
Integers and floating points are separated by the presence or absence of a decimal point: 
    5 is an integer whereas 5.0 is a floating point number.
'''
#Boolean Operators
#Operator	#Example
'not x	   Returns True if x is False; returns False otherwise.'
'x and y   Returns True if both x and y are True; returns False otherwise.'
'x or y	   Returns True if either x or y is True; returns False otherwise.'

# Python3 program for implementation 
# of int() function 
num = 13

String = '187'

# Stores the result value of
# binary "187" and num addition 
result_1 = int(String) + num 
print("int('187') + 13 = ", result_1, "\n")

# Example
str = '100'

print("int('100') with base 2 = ", int(str, 2))
print("int('100') with base 4 = ", int(str, 4))
print("int('100') with base 8 = ", int(str, 8))
print("int('100') with base 16 = ", int(str, 16))

#Floating Point Operators
'''
Symbol	            Meaning
+	                 Add
-	                 Subtract
*	                 Multiply
/	                 Divide
%	                 Modulo
**	                 Power
pow(x,y,[,z])	     Power with optional modulo (x**y)%z
abs(x)	             Absolute value
divmod(x,y)          Division with remainder
'''
#Additional functions are in the math module

import math
a = math.sqrt(x)
b = math.sin(x)
c = math.cos(x)
d = math.tan(x)
e = math.log(x)

#Commonly Used String Methods
'''
Methods	                                
Descriptions

s.count(substring, [start,end])	
Counts the occurrences of a substring with optional start and end parameters.

s.expandtabs([tabsize])	
Replaces tabs with spaces.

s.find(substring, [start, end])	
Returns the index of the first occurrence of a substring or returns -1 if the substring is not found.

s.isalnum()	
Returns True if all characters are alphanumeric; returns False otherwise.

s.isalpha()	
Returns True if all characters are alphabetic; returns False otherwise.

s.isdigit()	
Returns True if all characters are digits; returns False otherwise.

s.join(t)	
Joins the strings in sequence t.

s.lower()	
Converts the string to all lowercase.

s.replace(old, new [maxreplace])	
Replaces old substring with new substring.

s.strip([characters])	
Removes whitespace or optional characters.

s.split([separator], [maxsplit])	
Splits a string separated by whitespace or an optional separator. Returns a list.
'''

#String Escape Codes
'''
Symbol	Meaning
\n	Line feed
\r	Carriage return
\t	Tab
\xhh	Hexadecimal value
\”	Literal quote
\\	Backslash
'''
# Complex numbers
'''
Python complex numbers are of type complex. 
Every complex number contains one real part and one imaginary part.
'''
#example 
import cmath
c = I + 2j
print(type(c))
print(c)