# Cambie el salario de Ovinante a 8500

# Dado:

diccionario = {
    'emp1': {'nombre': 'Plantinancio', 'salario': 7500},
    'emp2': {'nombre': 'Herbijuan', 'salario': 8000},
    'emp3': {'nombre': 'Ovinante', 'salario': 6500}
    }

# Resultado:

# diccionario = {
#     'emp1': {'nombre': 'Plantinancio', 'salario': 7500},
#     'emp2': {'nombre': 'Herbijuan', 'salario': 8000},
#     'emp3': {'nombre': 'Ovinante', 'salario': 8500}
#     }

for (k,v) in diccionario.items():
    if v['nombre'] == 'Ovinante':
        v['salario'] = 8500
        break

print(diccionario)