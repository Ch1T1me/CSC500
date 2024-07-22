# Online Shopping Cart
class ItemToPurchase:
    def __init__(self, name = 'none', price = 0.0, quantity = 0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
   
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        return f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost:.2f}'

# part 2: prompt user to assign values to variables   
item1 = ItemToPurchase()
item2 = ItemToPurchase()

item1.item_name = input('Enter the item name:\n')
item1.item_price = float(input('Enter the item price:\n'))
item1.item_quantity = int(input('Enter the item quantity:\n'))
print()
item2.item_name = input('Enter the item name:\n')
item2.item_price = float(input('Enter the item price:\n'))
item2.item_quantity = int(input('Enter the item quantity:\n'))

# part 3: print values of each item
print()
print('TOTAL COST\n')
print(item1.print_item_cost())
print(item2.print_item_cost())

# print the totaled amounts
total_cost_item1 = item1.item_price * item1.item_quantity
total_cost_item2 = item2.item_price * item2.item_quantity

total_cost = total_cost_item1 + total_cost_item2
print(f'Total: ${total_cost:.2f}')