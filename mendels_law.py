
''' Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing 
a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate. '''



# consider k = AA , m = Bb and n = cc.


def dominant_probability(num_homozygous_dominant, num_heterozygous, num_homozygous_recessive): 
    total = num_homozygous_dominant + num_heterozygous + num_homozygous_recessive # Get the total population

# 	Every posssible combination from mating 2 'n' organisms will be recessive

    recessive_probability = (num_homozygous_recessive / total) * ((num_homozygous_recessive - 1) / (total - 1))
    
# By mating 'm' organisms, recessive outsprings will account for 25% of the total cases.    
    heterozygous_probability = (num_heterozygous / total) * ((num_heterozygous - 1) / (total - 1))
    hetero_recessive_probability = (num_heterozygous / total) * (num_homozygous_recessive / (total - 1)) + (num_homozygous_recessive / total) * (num_heterozygous / (total - 1))

# When mating 'm' and 'n' organisms 50% of the results will be recessive
    recessive_total = recessive_probability + heterozygous_probability * (.25) + hetero_recessive_probability * (.5)
    return (1 - recessive_total) # To get the answer we will subtract all the recessives from 100%



result = round(dominant_probability(29.0, 28.0, 20.0), 5) # Here insert the values for each type of oraganism to be taken into consideration. 
print(result)

