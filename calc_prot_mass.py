#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:49:55 2020

@author: alexandrubujor
"""

''' Function built to read the file and strip the unnecessary spaces '''

def readFile(filePath):
    with open(filePath, 'r') as f:
        return [white_space.strip() for white_space in f.readlines()] 
    
s = readFile(r'/Users/alexandrubujor/Downloads/rosalind_prtm.txt')





''' Transform the seq into a string '''

data = s[0]

single_aa = []

''' Build a list with individual Aminoacids '''

for char in data:
    single_aa.append(char)
    
    
    ''' Build a dictionary with the molecular mass for every aminoacid '''
    
aa_weight ={'A':'71.03711', 
            'C':'103.00919',
            'D':'115.02694',
            'E':'129.04259',
            'F':'147.06841',
            'G':'57.02146',
            'H':'137.05891',
            'I':'113.08406',
            'K':'128.09496',
            'L':'113.08406',
            'M':'131.04049',
            'N':'114.04293',
            'P':'97.05276',
            'Q':'128.05858',
            'R':'156.10111',
            'S':'87.03203',
            'T':'101.04768',
            'V':'99.06841',
            'W':'186.07931',
            'Y':'163.06333'   
    }

''' Made a list with the masses for every aminoacid found in the provided data '''
mass_aggregator = []

for x in single_aa:
    if x in aa_weight:
        mass_aggregator.append(aa_weight[x])

''' Calculate the sum of all elements found in the mass_aggregator list ''' 
protein_mass = 0
for y in mass_aggregator:
    protein_mass += float(y)
    
''' Print the result with only 3 decimals as the platform requests so. '''

result = round(float(protein_mass), 3)

print('The molecular mass for the provided protein sequence is:\n{result}'.format(result = result))




