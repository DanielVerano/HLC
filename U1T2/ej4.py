# Concatenar dos listas en el siguiente orden

lista1 = ["Hola ", "toma "]
lista2 = ["guapo", "señor"]

lista3 = []

for i in lista1:
    for j in lista2:
        lista3.append(i + j)

print(lista3)