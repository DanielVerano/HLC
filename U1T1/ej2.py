# Dadas dos cadenas, s1 y s2, cree una nueva cadena agregando s2 en medio de s1

s1 = "Hola"
s2 = "Adios"

mitad_s1 = int(len(s1) / 2)

nueva_cad = s1[0:mitad_s1] + s2 + s1[2:len(s1)]
print(nueva_cad)
