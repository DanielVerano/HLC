# Fusionar los siguientes dos diccionarios en uno

# Dado:

dict1 = {'Diez': 10, 'Veinte': 20, 'Treinta': 30}
dict2 = {'Treinta': 30, 'Cuarenta': 40, 'Cincuenta': 50}

# dict3 = dict1.copy()
# for n in dict2:
#     dict3[n] = dict2[n]

# **: Unpacking operator (expands dict content being the key-value pairs)
dict3 = {**dict1, **dict2}

print(dict3)