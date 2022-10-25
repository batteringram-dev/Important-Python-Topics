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

    # Calling out CSV file
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Item(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity')),
                )

    # This is Static method function
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10,0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


#Item.instantiate_from_csv()
#print(Item.all)

print(Item.is_integer(6))





