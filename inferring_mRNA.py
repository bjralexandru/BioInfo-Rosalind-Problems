########### Inferring mRNA from Protein ###########

'''
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the 
protein could have been translated, modulo 1,000,000. 
(Don't neglect the importance of the stop codon in protein translation.)

'''
 
 
protein = list(str(input('Protein seq: ')).upper()) 

prot_values = [] # Store the value of possible origins for every aminoacid in the given seq

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

''' Map the original dictionary and build a new dictionary but with number 
of possible codons that produce a certain aminoacid '''

frequency = {}

for k, v in prot_dict.items():
    if v not in frequency:
        frequency[v] = 0
    frequency[v] += 1
    

''' Get a list with all these values '''
for k,v in frequency.items():
    for char in protein:
        if char == k:
            prot_values.append(v)
        
            
prot_values.append(3) # 3 more possible combinations coming from the stop codon 

''' Multiply all the values from the list mod 1E6 '''
def listMultiplier(list):
    l =0 
    possib = 1
    for x in list:
        l = x
        possib = (possib * l) % 1000000
        
    
    return possib 

print('Number of possible parent sequences for that protein is: {} mod 1E6'.format(listMultiplier(prot_values)))