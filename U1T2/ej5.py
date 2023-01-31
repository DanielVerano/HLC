# Dada dos listas, itere ambas simultáneamente de modo que lista1 debería mostrar el elemento en el orden original y lista2 en orden inverso

lista1 = [10, 20, 30, 40]
lista2 = [100, 200, 300, 400]

lista2_inv = lista2.reverse()

for (x,y) in zip(lista1,lista2):
    print(f"{x} {y}")