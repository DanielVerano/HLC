# Cuente todas las minúsculas, mayúsculas, dígitos y símbolos especiales de una cadena determinada

str = "C@#he26ma^&amp;Du5ran"

num_caracteres = 0
num_digitos = 0
num_simbolos = 0

for x in str:
    if x.isalpha():
        num_caracteres = num_caracteres + 1
    elif x.isdigit():
        num_digitos = num_digitos + 1
    else:
        num_simbolos = num_simbolos + 1

print(f"Caracteres: {num_caracteres}")
print(f"Digitos: {num_digitos}")
print(f"Simbolos: {num_simbolos}")