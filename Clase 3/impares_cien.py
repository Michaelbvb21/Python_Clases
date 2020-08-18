# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:05:27 2020

@author: Cristhoffer Carrasco
"""


impares=[]
contador=1
numero=100

while contador<=numero:
    if contador % 2 !=0:
        impares.append(contador)
         
    contador=contador+1
    cantidad=len(impares)
print(impares)
print(f'la cantidad de numeros impares hasta {numero} es: {cantidad}')

    

        
    