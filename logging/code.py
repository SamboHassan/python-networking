import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def subtract(x, y):
    return x - y


num_1 = 10
num_2 = 4

add_result = add(num_1, num_2)
logging.debug("Add: {} + {} = {}".format(num_1, num_2, add_result))
multiply_result = multiply(num_1, num_2)
print("Mul: {} * {} = {}".format(num_1, num_2, multiply_result))
subtract_result = subtract(num_1, num_2)
print("Sub: {} - {} = {}".format(num_1, num_2, subtract_result))
