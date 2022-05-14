# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:24:03 2022

@author: ggZubrowka
"""

"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

def prime(limit):
    prime = []
    for i in range(2,limit+1):
        for j in range(2, int(limit**0.5)+1):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime

prime(600851475143)