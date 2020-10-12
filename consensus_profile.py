

# ====== PROBLEM DETAILS =======

#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
# ==============================


# GUIDE:
    # So it's not the best script for the given problem.
    # You get the ancestor DNA string prompted in the kernel (Nice! :D) 
    # But for the tabel that you must submit, you must go and open
    #   the .csv file, change the 'A C G T' with 'A: C: G: T:' to get the
    #     right answer on the web platform rosalind.info[CONS] problem. 
    #       (Not Nice!)





import numpy as np
import pandas as pd

''' Read the files, clean the data, isolate the DNA strings from the tag-lines''' 

def readFile(filePath):
    with open(filePath, 'r') as f:
        return [white_space.strip() for white_space in f.readlines()] 
    
data = readFile(r'/Users/alexandrubujor/Downloads/rosalind_cons-4.txt')


dictionar = {}

label = ""

dna_s = []

for line in data:
    if ">" in line:
        label = line
        dictionar[label] = ""
    else:
        dictionar[label] += line
        

for key,values in dictionar.items():
    dna_s.append(values)
    
''' Split the DNA strings letter by letter to build an array from every1'''

def splitWord(word):
    return[char for char in word]


dna_elem = []

for i in dna_s:
    string = splitWord(i)
    dna_elem.append(string)
    
DNA = np.array(dna_elem)
    
''' Count through the array columns to get how many nucleotides we've got from
each type.'''

a_count = np.count_nonzero(DNA == 'A', axis = 0)
c_count = np.count_nonzero(DNA == 'C', axis = 0)
g_count = np.count_nonzero(DNA == 'G', axis = 0)
t_count = np.count_nonzero(DNA == 'T', axis = 0)

''' Build a separate array with the nucleotides count. '''

profile = np.array([[a_count],[c_count],[g_count],[t_count]])

columns = [x for x in range(len(dna_s[0]))]

data = pd.DataFrame(data =profile[:,0] ,index = ['A', 'C', 'G','T'], columns = columns )

''' Get the winner nucleotide from each column and add it to a list '''
consensus = []

for col in columns:
    result = data[col].idxmax()
    consensus.append(result)
    
''' Pandas option to NOT hide the extra columns '''  
  
pd.set_option('display.max_columns', None)

''' Write the array data to a csv as it is easier to copy it from there '''

data.to_csv('rslnd-consensus.csv', header=False) # delete the header 'cause rosalind ain't needing it

''' Join the elements of the list to form the ancestor DNA string. '''

print(''.join(consensus)) 




