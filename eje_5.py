# Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
# Función para sumar todos los elementos de una lista
def sum_lista(lista):
    total = 0
    for num in lista:
        total += num
    return total

# Función para multiplicar todos los elementos de una lista
def multip_lista(lista):
    total = 1
    for num in lista:
        total *= num
    return total


numeros = [1, 2, 3, 4] #Numeros

# Mostrar el resultado de la suma y la multiplicación
print("La suma de los números es:", sum_lista(numeros))  # Resultado esperado: 10
print("La multiplicación de los números es:", multip_lista(numeros))  # Resultado esperado: 24
