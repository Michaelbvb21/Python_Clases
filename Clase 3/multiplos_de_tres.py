# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:27:27 2020

@author: Cristhoffer Carrasco
"""

numero=100
contador=1
i=0
while contador<=numero:
    if contador%3==0:
        print(contador)
        i=i+1
       
        
    contador=contador+1
    
print(f'La cantidad de multiplos de 3 es: {i}')