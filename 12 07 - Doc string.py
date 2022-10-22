# Write a python function to convert fahrenheit to celsius
# c = 5/9 * (f-32)

def fahrenheit_to_celsius(fahrenheit):
    """
    This function will convert fahrenheit to celsius
    :param fahrenheit: it takes fahrenheit temperature as parameters
    :return: this will return celsius temperature
    """
    celsius = 5/9 * (fahrenheit-32)
    return celsius
result = fahrenheit_to_celsius(99.8)
print(round(result, 2))
print(fahrenheit_to_celsius.__doc__)