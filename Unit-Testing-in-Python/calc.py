# Calculator for Unit Testing 

def add(x, y):
    # Adding function
    return x + y


def subtract(x, y):
    # Subtracting function
    return x - y


def multiply(x, y):
    # Multiplying function
    return x * y


def divide(x, y):
    # Dividing function
    if y == 0:
        raise ValueError('Can not divide by 0')
    else:
        return x / y



