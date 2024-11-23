# Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7])

# Función para imprimir un histograma
def procedimiento(lista):
    for numero in lista:
        # Imprimimos el número de asteriscos igual al valor del número en la lista
        print('*' * numero)

# Solicitar al usuario que ingrese una lista de números
entrada = input("Ingresa una lista de números  separados por espacios: ")

# Convertimos la entrada en una lista de enteros
lista_numeros = list(map(int, entrada.split()))

# Llamamos a la función para imprimir el histograma
procedimiento(lista_numeros)

