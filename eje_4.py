#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

# Función para verificar si un carácter es una vocal
def es_vocal(caracter):
    # Verificamos si el carácter es una vocal, en mayúsculas o minúsculas
    if caracter.lower() in 'aeiou':
        return True
    else:
        return False

# Prueba con input
caracter = input("Ingresa una letra (Vocal o no Vocal): ")

# Verificamos si el carácter es una vocal y mostramos el resultado
print(es_vocal(caracter))
