# Dada una lista, elimine todas las ocurrencias de 20 de la lista

lista = [5, 20, 15, 20, 25, 50, 20]

nueva_lista = [x for x in lista if x != 20];
print(nueva_lista)

# for x in lista:
#     if x == 20:
#         lista.remove(x)

print(lista)