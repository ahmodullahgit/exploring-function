"""
def add(a,b):
    return a+b
print(add(5,4))

def addition(a,b,c):
    return a+b+c
print(addition(4,6,8))
"""
"""
def multiple_number(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum
print(multiple_number(4,5,6,8,9,3,5, 12, 18))
"""
sentence_one = ['Hello, I\'m Ahmod. ',
                'Hi, I\'m Ahmod. ',
                'Hello, I\'m Ahmodullah. ',
                'Hi, I\'m Ahmodullah. ',
                'It\'s Ahmod here. ',
                'It\'s Ahmodullah here. '
                ]
sentence_two = [
    'I\'m 23 years old. ',
    'I\'m 23 years. ',
    'I\'m 23. ',
    'I\'m only 23. ',
    'i\'m still young, only 23. '
]
sentence_three = [
    'I live in Chapainawabgonj.',
    'I am from in Chapainawabgonj.',
    'My home is in Chapainawabgonj.',
    'My home town is in Chapainawabgonj.',
    'From Chapainawabgonj, the capital of mango.',
    'I am from Chapainawabgonj, the capital of mango.'
]
from random import choice
def templete(*args):
    paragraph = ''
    for sentence in args:
        paragraph = paragraph + choice(sentence)
    return f'<p>{paragraph}</p>'
print(templete(sentence_one, sentence_two, sentence_three))
