# Obtenga la clave de un valor mínimo del siguiente diccionario

# Dado:

diccionario = {
'Física': 82,
'Matemáticas': 65,
'Historia': 75
}

# Resultado:

# Matematicas

clave_minimo = ''
minimo = 0

for (x,y) in diccionario.items():
    if (minimo == 0):
        minimo = y
        clave_minimo = x
    elif (minimo > y):
        minimo = y
        clave_minimo = x

print(clave_minimo)