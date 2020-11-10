
########################## PROBLEM DETAILS ##############################


#Given: Six nonnegative integers, each of which does not exceed 20,000. 
#The integers correspond to the number of couples in a population 
#   possessing each genotype pairing for a given factor. 
#       In order, the six given integers represent the number of 
#           couples having the following genotypes:


# AA-AA = 1
# AA-Aa = 2
# AA-aa = 3
# Aa-Aa = 4
# Aa-aa = 5
# aa-aa = 6 ----> All organisms will have recessive alleles so we will ignore 
#                   this pair in our calculation.


#Return: The expected number of offspring displaying the dominant phenotype
# in the next generation, under the assumption that every couple has exactly
#  two offsprings.
# =======================================================================

# W = WEIGHT FOR EVERY TYPE OF ORGANISM IN THE TOTAL POPULATION

# E = EXPECTED RESULT FOR EVERY ORGANISM TYPE

W1, W2, W3, W4, W5 = 1, 0, 0, 1, 0


E1 = 2
E2 = 2
E3 = 2
E4 = 2 * 0.75 # Aa + Aa = [AA, Aa, Aa, aa] so 75% dominant containing offsprings
E5 = 2 * 0.5 # Aa + aa = [Aa,Aa,aa,aa] so 50% dominanat ...

result = E1*W1 + E2*W2 + E3*W3 + E4*W4 + E5*W5 

print(result)