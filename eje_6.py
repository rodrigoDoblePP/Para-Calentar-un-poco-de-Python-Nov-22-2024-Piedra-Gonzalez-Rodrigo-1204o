#Definir una función inversa() que calcule la inversión de una cadena.

# Función para invertir una cadena
def inversa(cadena):
    return cadena[::-1]  # El slicing [::-1] invierte la cadena

# Ejemplo de uso
cadena = input("Ingresa una cadena: ")

# Mostrar la cadena invertida
print("La cadena invertida es:", inversa(cadena))
