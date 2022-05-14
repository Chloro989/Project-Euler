# -*- coding: utf-8 -*-
"""
Created on Mon May  9 22:25:03 2022

@author: ggZubrowka
"""

for A in range(1,10):
    for B in range(0,10):
        for C in range(0,10):
            
            N = 100000*A+10000*B+1000*C+100*C+10*B+A

            print(f"\nN={N}")

            limit = N
            for i in range(100, limit+1):
                if N%i==0 & 99<i<1000 :
                    print(i, end = " ")
            
        
        

        



