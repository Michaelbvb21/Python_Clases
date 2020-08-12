# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:13:10 2020

@author: Cristhoffer Carrasco
"""

def divisible(numero,divisor1,divisor2):
    if numero%divisor1==0 and numero%divisor2==0:
        print(f'¡TRUE! El número {numero} es divisible por {divisor1} y {divisor2}')
    else:
        print(f'¡FALSE! El nÚmero no es divisible por estos números')
        
        
    
numero=int(input('Ingrese el número: '))
divisor1=int(input('Ingrese el primer divisor: '))
divisor2=int(input('Ingrese el segundo divisor: '))

divisible(numero,divisor1,divisor2)