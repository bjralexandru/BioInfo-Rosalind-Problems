import pandas as pd
import numpy as np 

l1 = ['A','C','G']

matrix = np.array([['C','C','G'],['C','G','T'],['T','T','T']])

print(matrix)

a_count = np.count_nonzero(matrix == 'A', axis = 0)
c_count = np.count_nonzero(matrix == 'C', axis = 0)
g_count = np.count_nonzero(matrix == 'G', axis = 0)
t_count = np.count_nonzero(matrix == 'T', axis = 0)

a1_count = list(a_count)
c1_count = list(c_count)
g1_count = list(g_count)
t1_count = list(t_count)

profile = np.array([[a_count],[c_count],[g_count],[t_count]])

columns = [x for x in range(3)]

data = pd.DataFrame(data =profile[:,0] ,index = ['A', 'C', 'G','T'], columns = columns )


consensus = []

for col in columns:
    result = data[col].idxmax()
    consensus.append(result)
    
print(''.join(consensus))
print(data[:1])

fg = open('rslnd.txt', 'a')
fg.write(''.join(consensus))
fg.write(str(data))
fg.close()