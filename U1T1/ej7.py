# Prueba de equilibrio de caracteres de cadena. Asumiremos que una cadena s1 y s2 está equilibrada si todos los caracteres de s1 están en s2. la posición de los caracteres no importa.

def equilibrada(s1, s2):
    # Recorremos los caracteres de s1
    for x in s1:
        # Si el caracter no se encuentra en s2 devolvemos falso
        if x not in s2:
            return False
    return True

s1 = "hDf"
s2 = "ChemaDuran"

print(equilibrada(s1, s2))