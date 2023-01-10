# Calcula la multiplicación y la suma de dos números. Dados dos números enteros, devuelve su producto sólo si el producto es mayor que 1000, de lo contrario, devuelve su suma.

num1 = int(input("Introduzca el primer número:"))
num2 = int(input("Introduzca el segundo número:"))

producto = num1 *  num2
suma = num1 + num2

if producto > 1000:
    print(producto)
else:
    print(suma)
