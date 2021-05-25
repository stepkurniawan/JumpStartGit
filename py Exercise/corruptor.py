#!/usr/bin/env python3

""" 
Accenture JumpStart
Python module

This script is a corruptor code that creates a corrupted data file for students to solve.
"""

__author__ = "Vladimir Nimec"
__version__ = "1.0.4"
__maintainer__ = "Vladimir Nimec"
__email__ = "vladimir.nimec@accenture.com"
__status__ = "Production"


import sys
import random

def randomizer(data, n=1):
    '''Return a random n values from a given list of data'''

    weights = random.choices([1, 1, 2, 3, 5, 8, 13], k=len(data))
    return random.choices(data, weights=weights, k=n)[0]


# definition of collection of value variation
As = ['a', 'ä', 'ae', 'A', 'Ä', 'AE', 'Ae']
comma = [':(', ':)', ':P', ':D']
Os = ['o', 'O', 'ö', 'Ö', 'oe', 'Oe']
dot = ['.', ',', '_']


def rand_cap(letter):
    '''Return a randomly selected upper or lower case of a letter'''

    return random.choice([letter.lower(), letter.upper()])


# open a source file
with open('source.txt', 'r') as f:
    content = ''.join(f.readlines())

# replace new line with commas (to have more fun :)
content = content.replace('\n', ',')

# initialize the resulting string variable
result = ''

# corrupt data one symbol at a time
for w in content:
    if w.lower() == 'a':
        result += randomizer(As)
    elif w == ',':
        result += randomizer(comma)
    elif w.lower() == 'o':
        result += randomizer(Os)
    elif w == '.':
        result += randomizer(dot)
    else:
        result += rand_cap(w)
        if random.uniform(0, 1) < 0.05:
            result += '&x0'

# write corrupted data to a new file
with open('corrupted_data', 'w') as wr:
    wr.write(result)