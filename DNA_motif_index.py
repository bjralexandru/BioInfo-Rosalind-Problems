#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:03:15 2020

@author: alexandrubujor
"""

''' Open the file containing the seq and the DNA motif '''
def readFile(filePath):
    with open(filePath, 'r') as f:
        return[white_space.strip() for white_space in f.readlines()] # Read and save doc files without the spaces

data = readFile('/Users/alexandrubujor/Downloads/rosalind_subs-3.txt')

print('The seq to be searched is: '+ data[0]+'\n')
print('DNA motif to be found is: '+ data[1]+'\n')

''' Separate the seq from the DNA motif '''

s = data[0]

t = data[1]

''' The core of the problem. Find all the possible positions in which the motif can be
found within the seq string. '''

py_response = [i for i in range(len(s)) if s.startswith(t, i)]


''' Transform the response in a normal counting way as in the Python syntax it will
start counting from 0 '''

normal_Response = []

for x in py_response:
    normal_Response.append(x+1)
    
''' Rosalind.info response formatting requests you output the indexes with spaces 
and no commas. '''


for y in normal_Response:
    
    print(y, end=" ")