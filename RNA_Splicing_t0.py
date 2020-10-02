# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:55:45 2020

@author: alexandru.bujor
"""

import re

def readFile(filePath):
    with open(filePath, 'r') as f:
        return [white_space.strip() for white_space in f.readlines()] 
    
data = readFile(r'C:\Users\alexandru.bujor\Downloads\rosalind_splc-3.txt')


dictionar = {}

label = ""

introns = []

for line in data:
    if ">" in line:
        label = line
        dictionar[label] = ""
    else:
        dictionar[label] += line
        

print(dictionar)

introns=list(dictionar.values())


dna_string = str(introns.pop(0))
print(dna_string)
print(introns)


for i in introns:
    try:
        new_dna_string = re.sub(i, '', new_dna_string)
    except NameError:
        new_dna_string = re.sub(i, '', dna_string)

print(new_dna_string)


nucleotides = ['A', 'C', 'G', 'T']



sx = list(sorted(set(new_dna_string)))

if sx != nucleotides:
    print('Incorrect sequence!')

RNA = new_dna_string.replace('T','U')

a=0
b=len(RNA)
codons = []


for i in range(0, len(RNA)):
    codons = [RNA[i:i+3] for i in range(a,b, 3)]
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


