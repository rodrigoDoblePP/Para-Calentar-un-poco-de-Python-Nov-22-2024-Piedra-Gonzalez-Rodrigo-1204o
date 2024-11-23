#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

# Función para generar una cadena con un carácter repetido n veces
def generar_n_caracteres(n, caracter):
    return caracter * n  # Multiplica el carácter por n y lo devuelve

# Solicitar entradas al usuario
n = int(input("Ingresa un número : "))  # Número de veces que se repetirá el carácter
caracter = input("Ingresa un carácter: ")  # El carácter a repetir

# Llamamos a la función y mostramos el resultado
resultado = generar_n_caracteres(n, caracter)
print("El resultado es:", resultado)

