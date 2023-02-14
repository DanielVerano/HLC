# Ordenar una tupla de tuplas por segundo elemento

tupla = (('a', 23),('b', 37),('c', 11),('d',29))

print(sorted(list(tupla), key=lambda x: x[1]))