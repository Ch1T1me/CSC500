# Online Shopping Cart
class ItemToPurchase:
    def __init__(self, name = 'none', price = 0.0, quantity = 0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
   
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        return f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost:.2f}'

# part 4: add new shoping cart class
class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
        self.customer_name = customer_name #attribute 1
        self.current_date = current_date #attribute 2
        self.cart_items = [] #attribute 3

    def add_item(self, item_to_purchase: ItemToPurchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name: str):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return           
        print('Item not found in cart. Nothing removed')
        
    def modify_item(self, item_to_purchase: ItemToPurchase):
        for item in self.cart_items:
            if item.item_name == item_to_purchase.item_name:
                if item_to_purchase.item_price != 0.0:
                    item.item_price = item_to_purchase.item_price
                if item_to_purchase.item_quantity != 0:
                    item.item_quantity = item_to_purchase.item_quantity
                return
        print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
        
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in 
        self.cart_items)

    def print_total(self):
        if not self.cart_items:
            print('SHOPPING CART IS EMPTY')
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
            total_items = self.get_num_items_in_cart()
            total_cost = self.get_cost_of_cart()
            print(f'Number of Items: {total_items}\n')
            for item in self.cart_items:
                print(item.print_item_cost())
            print(f'\nTotal: ${total_cost:.2f}')

    def print_descriptions(self):
        print(f'{self.customer_name} - {self.current_date}\n')
        print('Item Descriptions\n')
        for item in self.cart_items:
            description = getattr(item, 'description', 'No description available')
            print(f'{item.item_name}: {description}')

# part 5
def print_menu(shopping_cart: ShoppingCart):
    print('\nMENU')
    print('q - Quit\n')
    print('a - Add item to cart\n')
    print('r - Remove item from cart\n')
    print('c - Change item quantity\n')
    print('i - Output items\' descriptions\n')
    print('o - Output shopping cart\n')
    print('Choose an option: ', end='')

# def main: implement instructions for menu
def main():
    print('Welcome to the online Shopping Cart')
    #user input for name
    customer_name = input('Please enter your name: ')
    current_date = input('Please enter today\'s date: ')

    cart = ShoppingCart(customer_name, current_date)

    while True:
        print_menu(cart)
        # make sure there are no proceeding spaces and letters are lowercase
        choice = input().strip().lower()

        if choice == 'a':
            name = input('Enter item name:\n')
            description = input('Enter product description:\n')
            price = float(input('Enter the item price:\n'))
            quantity = int(input('Enter the item quantity:\n'))
            item = ItemToPurchase(name, price, quantity)
            item.description = description
            cart.add_item(item)
            print(f'Added {name} to cart.')
        
        elif choice == 'r':
            # remove item
            name = input('Enter item name to remove: ')
            cart.remove_item(name)
            print('Item removed')

        elif choice == 'c':
            # change item quantity
            name = input('Enter name of item you want to modify: ')
            new_quantity = int(input('Enter new quantity: '))
            item_to_modify = ItemToPurchase(name,0.0, new_quantity)
            cart.modify_item(item_to_modify)
            print('Item quantity modified to {new_quantity}')
        
        elif choice == 'i':
            cart.print_descriptions()

        elif choice == 'o':
            cart.print_total()    

        elif choice == 'q':
            # quit program
            print('Thank you for using the virtual shopping cart, enjoy :)')
            break
        else:
            print('Invalid option, plaese try again.')
# call main function to action
if __name__ == '__main__':
    main()