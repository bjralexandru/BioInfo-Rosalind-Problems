#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:16:14 2020

@author: alexandrubujor
"""

def mortal_fib(n,m):
    a = [0]*m
    a[-1] = 1
    
    for i in range(1, n):
        
        # Newborns
        
        new_rabbits = sum(a[:-1])
        
        # Shift ages left, i.e. getting older
        
        a[:-1] = a[1:] 
        # Assign newborns 
        
        a[-1] = new_rabbits
        
    return sum(a)


