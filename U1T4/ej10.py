# Compruebe si todos los elementos de la siguiente tupla son iguales

tupla = (45, 45, 45, 45)

primer_elem = tupla[0]
result = True

for x in tupla:
    if x != primer_elem:
        result = False

print(result)