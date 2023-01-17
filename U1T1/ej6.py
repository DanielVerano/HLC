# Dadas dos cadenas, s1 y s2, cree una cadena mixta usando las siguientes reglas

# Nota: Cree una tercera cadena hecha del primer carácter de s1, luego el último carácter de s2, Siguiente, el segundo carácter de s1 y el segundo último carácter de s2, y así sucesivamente. Los caracteres sobrantes van al final del resultado.

s1 = "Abc"
s2 = "Xyz"
resultado = ""

len_s1 = len(s1)
len_s2 = len(s2)

# Índice de s1 contando desde el principio
i_s1 = 0
# Índice de s2 contando desde el final
i_s2 = len(s2) - 1

# Mientras el índice de s1 sea menor a la longitud de s1 y a la longitud de s2
while i_s1 < len_s1 and i_s1 < len_s2:
    resultado += s1[i_s1] + s2[i_s2]
    i_s1 = i_s1 + 1
    i_s2 = i_s2 - 1

# Si el índice de s1 sigue siendo menor a su longitud, añadimos los caracteres restantes a resultado
while i_s1 < len_s1:
    resultado += s1[i_s1]
    i_s1 = i_s1 + 1

# Si el índice de s2 sigue siendo mayor que 0, añadimos los caracteres restantes a resultado
while i_s2 >= 0:
    resultado += s2[i_s2]
    i_s2 = i_s2 - 1

print(resultado)