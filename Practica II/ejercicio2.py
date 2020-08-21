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
        j=1
        for i in range(len(cadena)):
            if i!=0 and i%2!=0:
                car=cadena[i]
                lista_par.append(car)
                
    print(lista_par)            
        

    

    
    
cadena=input('Ingrese un cadena de texto: ')
caracter_par(cadena)