a = 32
b = 20

# addition = a + b
# subs = a - b
# print(addition, subs)

def multiple_return(a, b):
    """
    This will return addition and subtraction of two numbers
    :param a: first number
    :param b: second number
    :return: addition and subtraction
    """
    addition = a + b
    subs = a - b
    return addition, subs

print(multiple_return(40,25))
