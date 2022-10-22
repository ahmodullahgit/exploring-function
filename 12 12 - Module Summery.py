# function
'''
def function_name(parameters):
    """
    this is a test function for showing the syntax.
    :param parameters: this is a parameter
    :return: it will return as the statement.
    """
    statement
    return statement
'''

# Return ---> Where function will stop.
# Syntax
# Doc String

def rectangle_area(height, base):
    """
    this will calculate the area of a rectangle
    :param height: it takes a value which is height of rectangle
    :param base: it takes a value which is base of rectangle
    :return: this will return total area of a rectangle.
    """
    area = height * base
    return area
print(rectangle_area(5,6))
print(rectangle_area.__doc__)

def multiply(*args):
    result = 1
    for number in args:
        result *= number
    return result
print(multiply(1,3,4,6))