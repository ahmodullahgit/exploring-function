from random import choice

sentence_one = [
                'Former engineer for the People\'s Liberation Army Ren Zhengfei founded Huawei in 1987.',
                'Former People\'s Liberation Army engineer Ren Zhengfei founded Huawei in 1987.',
                'An engineer who had previously served in the People\'s Liberation Army founded Huawei in 1987. Ren Zhengfei.',
                'Former engineer in the People\'s Liberation Army Ren Zhengfei founded Huawei in 1987.'
]
sentence_two = [
                'It is the world\'s biggest producer of communications equipment.',
                'It is the biggest producer of communications equipment in the world.',
                'The world\'s largest manufacturer of communications equipment.',
                'It is the largest telecommunications equipment manufacturer in the world.'
]
sentence_three = [
    'Global Chinese networking, telecommunications equipment, and services business Huawei Ltd. is in the technology sector.',
    'Technology company Huawei Ltd. is a global Chinese networking,telecommunications equipment and services company.',
    'Chinese networking, telecommunications, and technology corporation Huawei Ltd. operates on a global scale.',
    'Chinese networking, telecommunications, and technology business Huawei Ltd. is a global player in these industries.'
]

# Random selection from sentences
# concatination of all sentences
# add html p tag

def paragraph_function(s1,s2,s3):
    """
    this will be a unique paragraph using random function.
    :param s1: this is the sentence one
    :param s2: this is the sentence two
    :param s3: this is the sentence three
    :return: this will return a paragraph with html <p>paragraph</p> tag
    """
    paragraph = choice(s1) + choice(s2) + choice(s3)
    return f'<p>{paragraph}</p>'

print(paragraph_function(sentence_one, sentence_two, sentence_three))
print(paragraph_function(sentence_one, sentence_two, sentence_three))
print(paragraph_function(sentence_one, sentence_two, sentence_three))

