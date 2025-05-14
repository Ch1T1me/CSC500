# total price of food at resturant
meal_price = int(input('Enter charged amount:\n'))

# calculations
tip = meal_price * 0.18
tax = meal_price * 0.07

# totaled
total_price = meal_price + tax + tip
print(f'The total amount spent at the resturant was: ${total_price:.2f}')
