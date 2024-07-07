# While Loop
'''
used to execute a block of statements repeatedly until a given condition is satisfied.
When the codition becomes false, the line after the loop IMMEDIATELY executes
'''
# INDENTATION USED TO GROUP STATEMENTS
'''
while expression:
    statement(s):
'''
count = 0
while (count < 3):
    count = count + 1
    print('Hello Geek')

# ELSE STATEMENTS W/ WHILE LOOP
''' 
while cndition:
    execute these statements
else:
    execute these statements
'''
count = 0
while (count < 3):
    count = count + 1
    print('Hello Geek')
else:
    print('In Else Block')


# INFINITE WHILE LOOP
count = 0
while (count == 0):
    print('Hello Geek')

# FOR IN LOOP 
'''
For Loop Syntax:
for iterator_var in sequence:
    statements(s)
'''
n = 4
for i in range(0, n):
    print(i)

print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),

'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

print('Initial savings of ${}'.format(initial_savings))
print('at {:.0f}% yearly interest.\n'.format(interest_rate*100))

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(' Savings at beginning of year {}: ${:.2f}'.format(i, savings))
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable

print('\n')

# As a general rule:
'''
Use a for loop when the number of iterations is computable before entering the loop, as when counting down from X to 0, printing a string N times, etc.
Use a for loop when accessing the elements of a container, as when adding 1 to every element in a list, or printing the key of every entry in a dict, etc.
Use a while loop when the number of iterations is not computable before entering the loop, as when iterating until a user enters a particular character.
'''

while expression:  # Loop expression
    # Loop body: Sub-statements to execute if 
    # the expression evaluated to True
    else:
    # Else body: Sub-statements to execute once 
    # if the expression evaluated to False

# Statements to execute after the loop
    
for name in iterable:
    # Loop body: Sub-statements to execute 
    # for each item in iterable
    else:
    # Else body: Sub-statements to execute 
    # once when loop completes

# Statements to execute after the loop


targetConsecutiveFreeThrows = 10
currentConsecutiveFreeThrows = 0
attempts = 0
makeFreeThrow = True
maxAttempts = 100  # Adding a max attempts to prevent infinite loop

while currentConsecutiveFreeThrows < targetConsecutiveFreeThrows and attempts < maxAttempts:
    attempts += 1
    if makeFreeThrow():  
        currentConsecutiveFreeThrows += 1
    else:
        currentConsecutiveFreeThrows = 0

print("Total Attempts to reach target: ", attempts)
