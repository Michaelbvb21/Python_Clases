# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 16:18:10 2020

@author: Cristhoffer Carrasco
"""
##Primera solución
"""

def mayor_menor(num1,num2,num3):
    
    if num1==num2 or num2==num3 or num1==num3:
        print('¡ALERTA! Los numeros ingresados son iguales')
    elif num1>num2 and num1>num3:
        if num2>num3:
            print(f'{num1} es mayor y {num3} es menor')
        else:
            print(f'{num1} es mayor y {num2} es menor')
    elif num2>num1 and num2>num3:
        if num1>num3:
            print(f'{num2} es mayor y {num3} es menor')
        else:
            print(f'{num2} es mayor y {num1} es menor')
    elif num3>num1 and num3>num2:
        if num1>num2:
            print(f'{num3} es mayor y {num2} es menor')
        else:
            print(f'{num3} es mayor y {num1} es menor')
 """    
##segunda solución
  
def mayor_menor(num1,num2,num3):
    if num1==num2 or num2==num3 or num1==num3:
        print('¡ALERTA! Los numeros ingresados son iguales')
        return 
    if num1>num2 and num1>num3:
        print(f'El número {num1} es mayor')
    elif num2>num3:
        print(f'El número {num2} es mayor')
    else:
        print(f'El número {num3} es mayor')
 
    if num1<num2 and num1<num3:
         print(f'El número {num1} es el menor ')
    elif num2<num3:
        print(f'El número {num2} es el menor ')
    else:
        print(f'El número {num3} es el menor ')
        

num1=float(input('Ingrese el primer número: '))
num2=float(input('Ingrese el segundo número: '))
num3=float(input('Ingrese el tercer número: '))

mayor_menor(num1,num2,num3)

