# Dada una lista, busque el valor 20 en la lista y, si está presente, reemplácelo con 200. Solo actualice la primera aparición de un valor

lista = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(lista)):
    if lista[i] == 20:
        lista[i] = 200
        break

print(lista)