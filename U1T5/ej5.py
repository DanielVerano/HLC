# Cree un nuevo diccionario extrayendo las siguientes claves de un diccionario a continuación

# Dado:

diccionario = {
    "nombre": "Pikolo",
    "edad":28,
    "salario": 8000,
    "planeta": "Namek"
    }

# Claves para extraer:
# keys = ["nombre", "salario"]

dict = {}

for k in diccionario.items():
    if (k[0] == 'nombre' or k[0] == 'salario'):
        dict[k[0]] = diccionario[k[0]]

print(dict)