# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:06:28 2020

@author: Cristhoffer Carrasco
"""

numero=100
cont=1
suma_par=0
suma_impar=0
pares=[]
impares=[]
while cont<=numero:
    if cont % 2 ==0:
        pares.append(cont)
        suma_par=suma_par+cont
    else:
        impares.append(cont)
        suma_impar+=cont
    cont=cont+1
print(pares)   
print(f'La suma de los pares es {suma_par}')
print(impares)
print(f'La suma de los impares es {suma_impar}')