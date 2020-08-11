# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:08:14 2020

@author: Cristhoffer Carrasco
"""

def par_impar(numero):
    if numero%2==0:
        print(f'El número {numero} es par')
    else:
        print(f'El número {numero} es impar')
        
numero=int(input('Ingrese un número: '))

par_impar(numero)