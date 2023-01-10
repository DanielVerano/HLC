# Acepte una lista de 5 números flotantes como entrada del usuario.

lista = []

for i in range(0, 5):
    num = float(input(f"Introduzca el número {i}: "))

    lista.append(num)

print(lista)