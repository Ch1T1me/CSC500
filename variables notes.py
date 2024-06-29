Datatypes
int (integers/numbers)
float (floating point numbers/decimals)
bool (booleans/ true or false)
str (strings/text)

example:
x = 3              # a whole number                   
f = 3.1415926      # a floating point number              
name = "Python"    # a string

print(x)
print(f)
print(name)

combination = name + " " + name
print(combination)

sum = f + f
print(sum)
------
run
3
3.1415926
Python
Python Python
6.2831852
------
COMPILER
Translates a high-level language program into low-level machine instructions.
A compiler ensures a program is valid according to the language's rules, performs optimizations, then converts to the low-level machine instructions.
Correct
APPLICATION
Another word for program.
The programmer-created sequence of instructions is called a program, application, or just app.
Correct
MACHINE INSTRUCTION
A series of 0s and 1s, stored in memory, that tells a processor to carry out a particular operation like a multiplication.
0s and 1s are hard to comprehend. Most programmers specify the program's functionality in a high-level language, which is then automatically translated to low-level machine instructions.
Correct
ASSEMBLY LANGUAGE
Human-readable processor instructions
An assembler is a program that translates assembly language instructions into machine instructions.
Correct

Table 1.6.1: Common error types.
Error type	Description
SyntaxError	The program contains invalid code that cannot be understood.
IndentationError	The lines of the program are not properly indented.
ValueError	An invalid value is used – can occur if giving letters to int().
NameError	The program tries to use a variable that does not exist.
TypeError	An operation uses incorrect types – can occur if adding an integer to a string.
