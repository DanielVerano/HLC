# Eliminar cadenas vacías de la lista de cadenas

lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]

lista2 = [x for x in lista if x != ""]

print(lista2)