# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:01:43 2020

@author: Cristhoffer Carrasco
"""

def mayor_cuatro(num1,num2,num3,num4):
    if num1==num2 or num2==num3 or num1==num3 or num1==num4 or num4==num2 or num4==num3:
        print('¡ALERTA! Los numeros ingresados son iguales')
        return
    if num1>num2 and num1>num3 and num1>num4:
        print(f'El número {num1} es mayor')
    elif num2>num3 and num2>num4:
        print(f'El número {num2} es mayor')
    elif num3>num4:
        print(f'El número {num3} es mayor')
    else:
        print(f'El número {num4} es mayor')
    
    
    if num1<num2 and num1<num3 and num1<num4:
        print(f'El número {num1} es menor')
    elif num2<num3 and num2<num4:
        print(f'El número {num2} es menor')
    elif num3<num4:
        print(f'El número {num3} es menor')
    else:
        print(f'El número {num4} es menor')
        
            




num1=float(input('Ingrese el primer número: '))
num2=float(input('Ingrese el segundo número: '))
num3=float(input('Ingrese el tercer número: '))
num4=float(input('Ingrese el cuarto número: '))


mayor_cuatro(num1,num2,num3,num4)