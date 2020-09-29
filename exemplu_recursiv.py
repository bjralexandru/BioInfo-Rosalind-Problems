# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:57:13 2020

@author: alexandru.bujor
"""
 
''' Input data n = number of months and k = number of litter pairs that one mature 
pair can give after 1 month '''
n = int(input('n: '))
k = int(input('k: '))

''' Recurssion function that will retrieve the number of rabbit pairs at the end of the given month! ''' 

def fact(n):
    if n <= 1:
        return 1
    else:
        return (fact(n-2)*k + fact(n-1))
    
rezultat = fact(n)

''' Getting the number of rabbit pairs at the beggining of the given month. '''

adapt = fact(n)-k*fact(n-2)

print(rezultat)
print(f'After {n} months, there will be {adapt} pairs of Wabbits!')