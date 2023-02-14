# Eliminar un conjunto de claves de un diccionario

# Dado:

diccionario = {
    "nombre": "Pikolo",
    "edad": 28,
    "salario": 8000,
    "planeta": "Namek"
    }

# keysToRemove = ["nombre", "salario"]

del diccionario["nombre"]
del diccionario["salario"]

print(diccionario)