#!/usr/bin/env python3

""" 
Accenture JumpStart
Python module

This script is a solution code to solve an excercise of cleaning corrupted data file
"""

__author__ = "Vladimir Nimec"
__version__ = "1.0.4"
__maintainer__ = "Vladimir Nimec"
__email__ = "vladimir.nimec@accenture.com"
__status__ = "Production"


import sys
import time


def read_file(file_path):
    '''Returns content of a file given in file path'''
    
    with open(file=file_path, mode='r') as f:
        # read content from file
        content = f.readlines()
    
    return content[0]


def clean_text(text):
    '''Cleans text from known garbage'''
    
    return text.replace('&x0', '')


def replace_wrong(text):
    '''Returns text with data replaces for known patterns'''

    clean_dict = {'o': ['ö', 'oe'],
                  'a': ['ä', 'ae'],
                  ';': [':(', ':)', ':p', ':d'],
                  '.': [',', '_']
                 }

    for key, value in clean_dict.items():
        for pattern in value:
            text = text.replace(pattern, key)

    return text


def reconstruct_structure(text, separator, num_columns):
    '''Returns a reconstructed data structure with num_columns number of columns'''

    structured = ''
    for i, element in enumerate(text.split(separator)):
        if (i + 1) % 4:
            structured += element + separator
        else:
            structured += element + '\n'
    
    return structured


def process_text(text):
    '''Returns a processed text'''

    # clean data from corrupted values
    cleaned_data = clean_text(text)

    # correct capitalization
    cleaned_data = cleaned_data.lower()

    # replace values with correct ones
    consistent_data = replace_wrong(cleaned_data)

    # reconstruct the original structure of data
    reconstructed_data = reconstruct_structure(consistent_data, ';', 4)

    return reconstructed_data    


def write_result(text, file):
    '''Writes result to file'''
    
    with open(file, 'w') as wf:
        wf.write(text)


def main(file_path):
    '''Main function that orchestrates all the actions'''

    print(f' > Processign file "{file_path}"')

    # load data
    content = read_file(file_path)
    # process data
    result = process_text(content)
   
    # write result to file
    write_result(result, 'result.csv')


if __name__ == '__main__':
    
    start = time.time()

    try:
        file_path = sys.argv[1]
    except:
        print(' > Please provide a source file path.')
        file_path = None

    # run main if file path is provided
    main(file_path)

    print(f' > Processed in {time.time() - start:.2} seconds.')