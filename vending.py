"""
vending.py
Defines the VendingMachine class which simulates a vending machine with
methods for managing items, money, and purchases
"""

class VendingMachine:
    """ A simple vending machine simulator that handles items, balance, and transactions. """

    def __init__(self):
        """ Initializes a new vending machine with an empty inventory, zero balance
            and no sales history. """
        self.vending_machine = []
        self.balance = 0
        self.total_sales = 0.0
        self.sales_history = []


    def add_item(self, name, price, quantity):
        """ Adds an item with name, price, and quantity to the vending machine.
            If the item already exists, increments its quantity """
        for item in self.vending_machine:
            if item['name'] == name:
                item['price'] = price
                item['quantity'] += quantity
                break
        else:
            self.vending_machine.append({'name': name, 'price': price, 'quantity': quantity})
        print(f'{quantity} {name}(s) added to inventory')

    
    def get_item_price(self, name):
        """ Returns the price of the specified item.
            Prints 'Invalid item' if the item does not exist in the vending machine. """
        for item in self.vending_machine:
            if item['name'] == name:
                return item['price']
        else:
            print('Invalid item')


    def get_item_quantity(self, name):
        """ Returns the quantity of the specified item.
            Prints 'Invalid item' if the item does not exist in the vending machine. """
        for item in self.vending_machine:
            if item['name'] == name:
                return item['quantity']
        else:
            print('Invalid item')
    

    def list_items(self):
        """ Returns a list of all items in the vending machine with their price and quantity.
            Prints 'No items in the vending machine' if the inventory is empty. """
        result = 'No items in the vending machine'
        if self.vending_machine:
            result = 'Available items:'
            for item in sorted(self.vending_machine, key=lambda item: item['name']):
                result += f'\n{item['name']} (${item['price']}): {item['quantity']} available'
        print(result)


    def insert_money(self, amt):
        """ Adds specified amount to the current balance.
            Prints 'Invalid amount' if the value is not $1, $2, or $5. """
        amt = float(amt)
        if amt == 1.0 or amt == 2.0 or amt == 5.0:
            self.balance += round(amt, 2)
            print(f'Balance: {self.balance}')
        else:
            print('Invalid amount')
    

    def purchase(self, name):
        """ Attemps to purchase the specified item from the vending machine.
            Checks stock and balance before completes the purchase.
            Updates sales history, balance, and item quantity. """
        for item in self.vending_machine:
            if item['name'] == name:
                if item['quantity'] == 0:
                    print(f'Sorry {name} is out of stock')
                elif self.balance >= item['price']:
                    # Deduct price and reduce quantity
                    item['quantity'] -= 1
                    self.balance = round(self.balance - item['price'], 2)
                    self.total_sales += item['price']
                    self.sales_history.append({'name': item['name'], 'price': item['price']})
                    print(f'Purchased {name}\nBalance: {self.balance}')
                else:
                    print(f'Insufficient balance. Price of {name} is {item['price']}')
                break
        else:
            print('Invalid item')
    

    def output_change(self):
        """ Returns the remaining balance as change and resets balance to 0.
            Prints 'No change' if there is no available balance. """
        if self.balance > 0:
            print(f'Change: {self.balance}')
            self.balance = 0
        else:
            print('No change')


    def remove_item(self, name):
        """ Removes the specified item from the vending machine inventory.
            Prints 'Invalid item' if not found. """
        for item in self.vending_machine:
            if item['name'] == name:
                self.vending_machine.remove(item)
                print(f'{name} removed from inventory')
                break
        else:
            print('Invalid item')
    

    def empty_inventory(self):
        """ Clears all items from the vending machine. """
        self.vending_machine.clear()
        print('Inventory cleared')
    

    def get_total_sales(self):
        """ Returns the total sales rounded to two decimal places. """
        return round(self.total_sales, 2)


    def stats(self, n):
        """ Prints sales stats for the most recent n purchases.
            Combines multiple purchases of the same item. """
        result = 'No sale history in the vending machine'
        if self.sales_history:
            if n > len(self.sales_history):
                result = f'Sale history for the most recent {len(self.sales_history)} purchase(s):'
            else:
                result = f'Sale history for the most recent {n} purchase(s):'
            combined_recent_purchases = []
            # Reverse to get most recent first
            self.sales_history.reverse()
            recent_purchases = [self.sales_history[i] for i in range(len(self.sales_history)) if i < n]
            for item in recent_purchases:
                for item2 in combined_recent_purchases:
                    if item['name'] == item2['name']:
                        item2['quantity'] += 1
                        item2['total_sale'] += item['price']
                        break
                else:
                    combined_recent_purchases.append({'name': item['name'], 'total_sale': item['price'], 'quantity': 1})
            for item in  sorted(combined_recent_purchases, key=lambda item: item['name']):
                result += f'\n{item['name']}: ${item['total_sale']} for {item['quantity']} purchase(s)'
        print(result)