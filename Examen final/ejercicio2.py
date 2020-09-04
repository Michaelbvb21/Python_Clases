# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:07:51 2020

@author: Cristhoffer Carrasco
"""


class Matriz():
    def __init__(self, tamaño):
        self.tamaño = tamaño

    def crear_lista (self):
        matriz=[]
        for i in range(self.tamaño):
            matriz.append(i)

        return matriz

matriz1 = Matriz(10)
print(matriz1.crear_lista())