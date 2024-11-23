#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

# Función para verificar si dos listas tienen al menos un miembro en común
def superposicion(lista1, lista2):
    # Recorremos cada elemento de la primera lista
    for elemento1 in lista1:
        # Recorremos cada elemento de la segunda lista
        for elemento2 in lista2:
            # Si encontramos un elemento común, devolvemos True
            if elemento1 == elemento2:
                return True
    # Si no encontramos ningún elemento común, devolvemos False
    return False

# Ejemplo de uso
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 3]

# Verificar si las listas tienen al menos un miembro en común
if superposicion(lista1, lista2):
    print("Las listas tienen al menos un miembro en común.")
else:
    print("Las listas no tienen miembros en común.")
