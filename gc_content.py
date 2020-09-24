
"""
Created on Mon Sep 21 17:26:44 2020

@author: alexandrubujor
"""

# Build a function to open, read and strip the white space in the file containing the seq :
def readFile(filePath):
    with open(filePath, 'r') as f:
        return [white_space.strip() for white_space in f.readlines()] 
    
   
# Easy math eq to calculate the content - (procent wise) of "G" and "C" letters in the bigger seq.
def gc_content(seq):
    return round ((((seq.count('C')+seq.count('G'))/len(seq))*100), 6)

data = readFile('/Users/alexandrubujor/Downloads/rosalind_gc.txt')


# The strategy is to build a dictionary that saves the FASTA format tag line as a label for the dictionary
# And the string that is the seq as a key for that label
# We need to clean the data in this way so at the end we can also retrieve the biggest percentage of GC content
# and also the tag >Rosalind_xxxx that it belongs to
dictionar = {}

label = ""

for line in data:
    if ">" in line:
        label = line
        dictionar[label] = ""
    else:
        dictionar[label] += line


# Format the result to match the '>Rosalind_xyzw : Percentage' format   
rezultat = {key: gc_content(value) for (key,value) in dictionar.items()}

print(rezultat)

maximul = max(rezultat, key=rezultat.get)

# Format the result to be printed in the ROSALIND.info format


print(maximul)

print(f'{maximul[1:]}\n{rezultat[maximul]}')
