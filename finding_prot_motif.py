''' FINDING PROTEIN MOTIF '''

''' For example, the data for protein B5ZC00 can be found at 
http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output 
its given access ID followed by a list of locations in the protein string 
where the motif can be found. '''


import urllib.request
import re

''' INSERT LIST OF UNIPROT_IDS '''

def readFile(filePath):
    with open(filePath, 'r') as f:
        return [white_space.strip() for white_space in f.readlines()] 
    
uniprot_id = []
rosalind_data = readFile('directoryPath/rosalind_mprt-2.txt')

for line in rosalind_data:
    uniprot_id.append(line)
    
''' CREATE FILES WITH THE FASTA CONTENT RETRIEVED FROM THE WEBSITE '''

for i in uniprot_id:
    x = uniprot_id.index(i)
    url = 'https://www.uniprot.org/uniprot/{uniprot_id}.fasta'.format(uniprot_id = uniprot_id[x])
    urllib.request.urlretrieve(url, 'path-Where-to-save-files/{uniprot_id}.fasta'.format(uniprot_id = uniprot_id[x]))

''' READ FASTA FILES LIKE IN THE OTHER EXERCISES deleting whitespace and building 
    dictionary with '>....' : 'QWERTY' pairs '''
    
dictionar = {}
label = ""   

for i in uniprot_id:
    x = uniprot_id.index(i)
    data = readFile(r'path-Where-you-saved-the-FASTA-files/{uniprot_id}.fasta'.format(uniprot_id = uniprot_id[x]))

    for line in data:
        if '>' in line:
            label = line
            dictionar[label] = ""
        else:
            dictionar[label] += line

''' CHANGE THE KEYS FROM THE FASTA FILE WITH THE CLEANER UNIPROD-ID-S '''

for key,new_key in zip(list(dictionar), uniprot_id):
        dictionar[new_key] = dictionar.pop(key)

''' ALL THE MOJO IS IN THIS REGEX. DID THE REGEX USING REGEX101 WEBSITE TO MATCH

    THE N-glycosylation motif NAMELY N{P}[ST]{P}. NEXT USE THE RE.FINDITER'S FUNCTION MATCH.START() TO
    
    GET THE STARTING POSITION FOR EVERY MATCH AND FOR OVERLAPING MATCHES'''

for k,v in dictionar.items():

     dictionar[k] = [x.start()+1 for x in re.finditer("(?=N[^P][ST][^P])", v)]


''' PRINT RESULTS SPECIALLY FOR ROSALIND SUBMISSION EXCEPT THAT YOU WILL HAVE TO DELETE
    THE ROWS CONTAINING PROTEINS FOR WHICH WE HAVE NO MATCH FOR THE N-GLYCO MOTIF. 
    
    IF YOU DON'T DELETE THEM, IT WILL GIVE A WRONG ANSWER ON THEIR PLATFORM.'''
    
for k,v in dictionar.items():
    print('{}'.format(k))
   
    print(*v, sep=' ') # *v will print the result on a different row with spaces 
                            # and no brackets 