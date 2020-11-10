#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:53:25 2020

@author: alexandrubujor
"""

''' Use itertools library for the efficent loop through the possible permutations '''
import itertools

n = int(input('Select number of elements: '))

''' Generate a list of consecutive elements with a given number '''

x = list(range(n))

x.pop(0)    # Make sure it starts with 1 '''
x.append(n) #And it also contains the last number of the list '''

print(x)

total_permutations = 1

for p in x:
    total_permutations*= p
print(total_permutations)  # Here I calculate the possible number of permutations using the formula P(n) = n! '''

a = list(itertools.permutations(x)) # The itertools module for the permutations loop '''

for char in a:
    print(' '.join(str(xyz) for xyz in char)) # Print the results with the ROSALIND.info template

 