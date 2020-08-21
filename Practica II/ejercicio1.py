# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:06:47 2020

@author: Cristhoffer Carrasco
"""


def check_examen(resp_correctas,resp_enviadas):
    nota=0
    for i in range(4):
        if resp_enviadas[i]==resp_correctas[i]:
            nota=nota+4
        elif resp_enviadas[i]=='':
            nota=nota+0
        else:
            nota=nota-1
    print(f'La nota del alumno es {nota}')        
    
    
resp_correctas=['a','c','d','b']
resp_enviadas=['a','d','','b']

check_examen(resp_correctas,resp_enviadas)