#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:07:17 2020

@author: alexandrubujor
"""

def readFile(filePath):
    with open(filePath, 'r') as f:
        return[white_space.strip() for white_space in f.readlines()] # Read and save doc files without the spaces

data = readFile('/Users/alexandrubujor/Downloads/rosalind_hamm.txt')

print(data)

s = list(data[0]) # We know there are 2 genes in the file so we split them in separate variables
t = list(data[1])

p = zip(s,t)

print(p) #wanted to test the zip function to try and understand how the function works

counter = 0 

for char,xyz in zip(s,t):
    if char != xyz:
        counter += 1 # count the differences in the 2 strings letter by letter
print(counter)

    

    


   
