# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:18:26 2020

@author: Cristhoffer Carrasco
"""



def caracter_par(cadena):
    lista_par=[]
    if len(cadena)>100 or len(cadena)<2:
        print('Cadena no valida')
    else:
        for i in cadena:
            lista_par.append(i+1)
            print(lista_par)
    

    

    
    
cadena=input('Ingrese un cadena de texto: ')
caracter_par(cadena)