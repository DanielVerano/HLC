# Dada una cadena de entrada con la combinación de mayúsculas y minúsculas,organice los caracteres de tal manera que todas las letras minúsculas deben ir primero.

str = "ChEmaDUraN"

minusculas = ""
mayusculas = ""

for x in str:
    if x == x.lower():
        minusculas += x
    else:
        mayusculas += x

print(minusculas + mayusculas)
