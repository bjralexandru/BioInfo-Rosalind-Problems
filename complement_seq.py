#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 18:41:20 2020

@author: alexandrubujor
"""
s = input('Copy-paste the sequence: ')

sl = list(s)



''' First we obtain a reversed version of the sequence because that's how you start when you want to get
    the complementary one. '''

sr = list(reversed(s))



''' Built some working but inefficient for-loops to change every nucleotide in the seq with the complementary 
    one. '''

for char in sr:
    if char == 'T':
        x = sr.index(char)
        sr[x] = 'X'


for char in sr:
    if char == 'A':
        y = sr.index(char)
        sr[y] = 'Y'


for char in sr:
    if char == 'C':
        z = sr.index(char)
        sr[z] = 'Z'       


for char in sr:
    if char == 'G':
        w = sr.index(char)
        sr[w] = 'W'

sc = ''.join(sr)

sc = sc.replace('X','A')
sc = sc.replace('Y','T')
sc = sc.replace('Z','G')
sc = sc.replace('W','C')

print(f'The complementary seq is: \n' + sc)





    

    
