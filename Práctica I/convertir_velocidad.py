# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:04:37 2020

@author: Cristhoffer Carrasco
"""

#factor de conversion: 1000/36

def convertir(velocidad):
    velocidad_cm_s=velocidad*1000//36
    print(f'La velocidad en cm por segundo es {velocidad_cm_s} cm/s')
 
    
velocidad=float(input('Escriba la velocidad en km/h: '))

convertir(velocidad)
