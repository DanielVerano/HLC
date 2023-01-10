# Acepte tres cadenas cualquiera de una llamada input(). Escriba un programa para tomar tres nombres como entrada de un usuario con una única llamada a función input().

cadenas = input("Introduzca tres cadenas separadas por un espacio:")
# nom1, nom2, nom3 = input("Introduzca tres nombres: ").split()

list = cadenas.split()

print(list)