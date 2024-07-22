# Iterating over multi-dimensional lists.
currency = [

        [1.00, 5.00, 10.0], # US Dollars
        [0.75, 3.77, 7.53], # Euros
        [0.65, 3.25, 6.50]  # British pounds
]

for row in currency:
    for cell in row:
        print(cell, end=' ')
    print()

# Iterating through multi-dimensional lists using enumerate().
currency = [
   [1, 5, 10 ],  # US Dollars
   [0.75, 3.77, 7.53],  #Euros
   [0.65, 3.25, 6.50]  # British pounds
]
for row_index, row in enumerate(currency):
   for column_index, item in enumerate(row):
       print('currency[{}][{}] is {:.2f}'.format(row_index, column_index, item))

# list comprehension
new_list = ['expression' for name in 'iterable']  
    # componenets
'''
An expression component to evaluate for each element in the iterable object.
A loop variable component to bind to the current iteration element.
An iterable object component to iterate over 
(list, string, tuple, enumerate, etc).
'''
my_list = [10, 20, 30]
list_plus_5 = [(i + 5) for i in my_list]

print('New list contains:', list_plus_5)

# Use list() to convert view objects into lists.
solar_distances = dict(mars=219.7e6, venus=116.4e6, jupiter=546e6, pluto=2.95e9)
list_of_distances = list(solar_distances.values())  # Convert view to list

sorted_distance_list = sorted(list_of_distances)
closest = sorted_distance_list[0]
next_closest = sorted_distance_list[1]

print('Closest planet is {:.4e}'.format(closest))
print('Second closest planet is {:.4e}'.format(next_closest))

# dict.items() – returns a view object that yields (key, value) tuples.
dict.items()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda, calories in num_calories.items():
    print('{}: {}'.format(soda, calories))

# dict.keys() – returns a view object that yields dictionary keys.
dict.keys()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.keys():
    print(soda)

# dict.values() – returns a view object that yields dictionary values.
dict.values()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.values():
    print(soda)