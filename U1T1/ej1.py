# Dada una cadena de longitud impar mayor que 7, devuelva una nueva cadena formada por los tres caracteres del medio de una cadena determinada

import math

cadena = input("Introduzca una cadena de longitud impar mayor que 7: ")

if len(cadena) >= 7 and len(cadena) % 2 != 0:
    mitad = math.trunc(len(cadena) / 2)
    mitad_inferior = mitad - 1
    mitad_superior = mitad + 1
    
    print(cadena[mitad_inferior:mitad_superior+1])
else:
    print("Cadena no válida")