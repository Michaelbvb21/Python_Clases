# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:46:27 2020

@author: Cristhoffer Carrasco
"""


def area_perimetro(ancho,largo):
    if ancho==largo:
        area=ancho**2
        print(f'Es un cuadrado. Su área es {area} m2')
    else:
        perimetro=2*(ancho+largo)
        print(f'Es un rectangulo. Su perimetro es {perimetro} m')

ancho=float(input('Ingrese el ancho en metros: '))
largo=float(input('Ingrese el largo en metros: '))

area_perimetro(ancho,largo)