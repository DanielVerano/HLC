# Copie los elementos 44 y 55 de la siguiente tupla en una nueva tupla

tupla = (11, 22, 33, 44, 55, 66)

result = tuple([n for n in tupla if n == 44 or n == 55])

print(result)