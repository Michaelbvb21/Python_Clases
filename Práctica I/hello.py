# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:45:44 2020

@author: Cristhoffer Carrasco
"""


def hello(nombre):
    if nombre!='':
        print(f'Hola, {nombre}!')
    else:
        print('Hola mundo!')
        
nombre=input('Ingrese un nombre: ')
hello(nombre)