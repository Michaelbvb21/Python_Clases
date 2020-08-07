# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 20:10:44 2020

@author: Cristhoffer Carrasco
"""


def convertir_moneda(tipo_de_cambio,moneda):
    monto=float(input(f"Ingrese el monto en {moneda}: "))
    monto_dolares=round(monto*tipo_de_cambio,2 )
    print(f"El monto en dolares es: {monto_dolares}")

mensaje="""
Hola, este es un conversor de monedas
Ingrese cualquier de estas 3 opciones:
1=soles - dolares
2=Euros - dolares
3=Pesos colombianos - dolares
"""
    
print(mensaje)

opcion=int(input("Ingresa la opción: "))

if opcion==1:
    convertir_moneda(0.28,"soles")
elif opcion==2:
    convertir_moneda(1.19,"euros")
elif opcion==3:
    convertir_moneda(0.00027,"Pesos colombianos")
