#3 - Definir una función que calcule la longitud de una lista o una cadena dada.
# Función isnum para verificar si un valor es un número

# Función para verificar si es un número
def isnum(a):
    try:
        int(a)  # Intenta convertir a entero
        return True
    except:
        return False

# Función para calcular la longitud o devolver el número
def length(a):
    if not isnum(a):  # Si no es un número, devuelve la longitud de la cadena
        return len(a)
    else:  # Si es un número, devuelve el mismo número
        return a

# Pedir un valor al usuario
entrada = input("Ingresa un caracter o una cadena,lo que gustas : ")

# Mostrar el resultado de la función length
print("El resultado es:", length(entrada))
