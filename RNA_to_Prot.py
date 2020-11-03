# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:51:21 2020

@author: alexandru.bujor
"""

''' Read the file containing the seq '''

def readFile(filePath):
    with open(filePath, 'r') as f:
        return [white_space.strip() for white_space in f.readlines()] 
    
s = ['AUGGCU']

''' Transform the seq into a string '''

data = s[0]

''' Split the original seq in codons of 3 nucleotides '''

a=0
b=len(data)

codons = []


for i in range(0, len(data)):
    codons = [data[i:i+3] for i in range(a,b, 3)]
print(codons)

''' Identify the codons and substitute them with the corresponding protein
symbol.'''

protein = []
prot_dict ={'UUU':'F',  'CUU':'L',  'AUU':'I',  'GUU':'V',
            'UUC':'F',  'CUC':'L',  'AUC':'I',  'GUC':'V',
            'UUA':'L',  'CUA':'L',  'AUA':'I',  'GUA':'V',
            'UUG':'L',  'CUG':'L',  'AUG':'M',  'GUG':'V',
            'UCU':'S',  'CCU':'P',  'ACU':'T',  'GCU':'A',
            'UCC':'S',  'CCC':'P',  'ACC':'T',  'GCC':'A',
            'UCA':'S',  'CCA':'P',  'ACA':'T',  'GCA':'A',
            'UCG':'S',  'CCG':'P',  'ACG':'T',  'GCG':'A',
            'UAU':'Y',  'CAU':'H',  'AAU':'N',  'GAU':'D',
            'UAC':'Y',  'CAC':'H',  'AAC':'N',  'GAC':'D',
            'UAA':' ',  'CAA':'Q',  'AAA':'K',  'GAA':'E',
            'UAG':' ',  'CAG':'Q',  'AAG':'K',  'GAG':'E',
            'UGU':'C',  'CGU':'R',  'AGU':'S',  'GGU':'G',
            'UGC':'C',  'CGC':'R',  'AGC':'S',  'GGC':'G',
            'UGA':' ',  'CGA':'R',  'AGA':'R',  'GGA':'G',
            'UGG':'W',  'CGG':'R',  'AGG':'R',  'GGG':'G',  
    } 

for char in codons:
    if char in prot_dict:
        protein.append(prot_dict[str(char)])
    
''' Print the result into a word. '''
        
print(''.join(protein))