# Compruebe si existe un valor 200 en un diccionario

# Dado:

diccionario = {'a': 100, 'b': 200, 'c': 300}

# Resultado:

# True

existe = False
for x in diccionario.values():
    if x == 200:
        existe = True
print(existe)