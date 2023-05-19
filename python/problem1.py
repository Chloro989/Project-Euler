# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:07:20 2022

@author: ggZubrowka
"""

"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000."""

global N
N = 1000

sum_list = []


def multiples():
    
   for i in range(0, N):
        if i%3 ==0 or i%5 ==0:
            sum_list.append(i)
            
   print(sum(sum_list))
   
multiples()
    

            
        
            


