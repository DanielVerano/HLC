# Dada una cadena de entrada, cuente las apariciones de todos los caracteres dentro de una cadena

str = "Apple"

def apariciones_caracteres(str=""):
    # Objeto en el que se asociará cada caracter con el número de apariciones
    resultado = {}

    # Recorremos los caracteres de la cadena
    for x in str:
        # Si el caracter ya existe en el objeto, incrementamos su contador por 1
        if x in resultado:
            resultado[x] = resultado[x] + 1
        # Si no existe, creamos su contador inicialmente a 1
        else:
            resultado[x] = 1
    return resultado

print(apariciones_caracteres(str))