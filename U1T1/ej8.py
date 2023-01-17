# Busque todas las apariciones de "que" en una cadena dada, independientemente que esté o no en mayúsculas.

str = "Lo que yo te diga. Que la vida es así"

def apariciones(cadena=""):
    num = 0
    # Pasamos la cadena a minúsculas, ya que para el ejercicio no nos importa el case sensitive
    cadena = cadena.lower()
    # Creamos un array con todas las palabras de la cadena
    palabras = cadena.split(" ")

    # Recorremos las palabras de la cadena
    for x in palabras:
        # Si la palabra coincide con 'que' incrementamos la variable 'num'
        if x == "que":
            num = num + 1
    return num

print(f"El recuento de 'que' es: {apariciones(str)}")