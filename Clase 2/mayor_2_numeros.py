# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:29:14 2020

@author: Cristhoffer Carrasco
"""

"""
Ejercicio1 condicionales
"""

def mayor(num1, num2 ):
  if num1>num2:
    resultado=print(f"El número mayor es {num1}")
  elif num1<num2:
    resultado=print(f"El número mayor es {num2}")
  return resultado

a=float(input('Ingrese el primer número: '))
b=float(input('Ingrese el segundo número: '))

mayor(a,b)


