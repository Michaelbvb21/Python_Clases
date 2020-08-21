# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:18:22 2020

@author: Cristhoffer Carrasco
"""

frase=input('Ingrese una frase: ')
letra=input('Ingrese la letra que desea contar: ')
j=0
for i in frase:
    
    if i==letra:
        j=j+1
print(f'El número de veces que se repite la letra {letra} es: {j}') 

