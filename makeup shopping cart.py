Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
...         total = self.item_price * self.item_quantity
... 
>>> print("Look inside your shopping cart")
Look inside your shopping cart
>>> # Item 1
>>> print("\nItem 1")

Item 1
>>> item1 = ItemToPurchase()
>>> item1.item_name = input("What makeup are you looking for? ")
What makeup are you looking for? Blush
>>> item1.item_price = float(input("Enter the cost? "))
Enter the cost? 64
>>> item1.item_quantity = int(input("Amount added to cart? "))
Amount added to cart? 2
>>> 
>>> # Item 2
>>> print("\nItem 2")

Item 2
>>> item2 = ItemToPurchase()
>>> item2.item_name = input("What makeup are you looking for? ")
What makeup are you looking for? Lipstick
>>> item2.item_price = float(input("Enter the cost? "))
Enter the cost? 29
>>> item2.item_quantity = int(input("Amount added to cart? "))
Amount added to cart? 5
>>> 
>>> # Show total
>>> print("\nTotal Cost")

Total Cost
>>> item1.print_item_cost()
>>> item2.print_item_cost()
>>> 
>>> total_cost = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
>>> print(f"Total: ${total_cost:.2f}")
Total: $273.00
