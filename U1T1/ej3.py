# Dadas dos cadenas, s1 y s2 devuelven una nueva cadena compuesta por el primer, el medio y el último carácter de cada cadena de entrada

s1 = "Chema"
s2 = "Duran"

mitad_s1 = int(len(s1) / 2)
mitad_s2 = int(len(s2) / 2)

resultado = s1[0]+s2[0]+s1[mitad_s1]+s2[mitad_s2]+s1[len(s1)-1]+s2[len(s2)-1]
print(resultado)