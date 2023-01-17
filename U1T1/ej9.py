# Dada una cadena, devuelve la suma y el promedio de los dígitos que aparecen en la cadena, ignorando todos los demás caracteres.

str = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"
str = str.split(" ")

suma = 0
digitos = 0

for x in str:
    if x.isdigit():
        suma += int(x)
        digitos = digitos + 1

print(f"La suma es {suma}")
print(f"El promedio es {suma / digitos}")
