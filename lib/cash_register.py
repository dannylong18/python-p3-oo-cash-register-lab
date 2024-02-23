#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount = 0, total = 0, items = None):
        self.discount = discount
        self.total = total
        self.items = items if items is not None else []

    def add_item(self, title, price, quantity = 1):
        if quantity >= 1:
            for _ in range(quantity):
              self.items.append(title)
            price = quantity * price
        self.total += price 
        self.last_transaction = price

        
    def apply_discount(self):
        if self.discount:
            dollar_discount = self.discount/100 * self.total
            self.total -= dollar_discount
            print(f'After the discount, the total comes to ${int(self.total)}.')        
        else:
            print('There is no discount to apply.')

    def void_last_transaction(self):
        self.total = self.total - self.last_transaction