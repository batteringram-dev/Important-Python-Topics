import csv

# Classes in Object-Oriented Programming

# The init constructor will call an object
class Item():
    all = []
    # This is a Class Attribute
    pay_rate = 0.8 # Pay rate after 20 % discount
    def __init__(self, name, price, quantity):
        # Validations that the Price and Quantity are greater than or equal to Zero
        # We can set our own exception messages
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Self - Assigning the attributes from the init method
        self.name = name
        self.price = price
        self.quantity = quantity

        # Appending all into the all list
        Item.all.append(self)

    # Multiplying the Price and Quantity
    def calculate_total_price(self):
        return self.price * self.quantity

    # Reason why I added self to Pay rate is that we can change the pay rate from the Instance level
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # Repr - Representing our object
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get('name'),
                    price=item.get('price'),
                    quantity=item.get('quantity'),
                )



item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

# Defining our Instance 1
# Here we have not changed the pay rate, so it takes it from the Class level
# item1 = Item("Phone", 100, 1)
# item1.apply_discount()
# print(item1.price)

# Defining our Instance 2
# Here we are defining our pay rate, so it doesn't take the pay rate from the Class level
# item2 = Item("Laptop", 1000, 1)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)


