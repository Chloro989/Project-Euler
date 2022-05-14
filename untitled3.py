# -*- coding: utf-8 -*-
"""
Created on Mon May  9 21:49:08 2022

@author: ggZubrowka
"""

def divideByFactor(factor, num):
  while(num % factor == 0): #割り切れなくなるまで割る
    num /= factor
  return factor, num

num = 600851475143
factor =1

while num >= factor:
  factor += 1
  factor, num = divideByFactor(factor, num)

print(factor)