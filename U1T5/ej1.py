# A continuación se muestran las dos listas, conviértalo en el diccionario

keys = ['Diez', 'Veinte', 'Treinta']
values = [10, 20, 30]

dict = {keys[i]: values[i] for i in range(len(keys))}

print(dict)