"Points Awarded by CSU Bookstore"

# enter valid input
valid_input = False
while not valid_input:
    books = int(input('Enter books purchased this month' 
                      '(valid numbers are: 0, 2, 4, 6, 8 or more):\n'))
    if books in [0, 2, 4, 6] or books >= 8:
        valid_input = True
    else:
        print('Invalid input. Enter either 0, 2, 4, 6, or 8 or more')

# set criteria for total books_purchased:
if books == 2:
    print(f'This month you purchased {books} books, you earn 5 points')
elif books == 4:
    print(f'This month you purchased {books} books, you earn 15 points')
elif books == 6:
    print(f'This month you purchased {books} books, you earn 30 points')
elif books >= 8:
    print(f'This month you purchased {books} books, you earn 60 points')
else:
    print(f'This month you purchased {books} books, you earn 0 points')
