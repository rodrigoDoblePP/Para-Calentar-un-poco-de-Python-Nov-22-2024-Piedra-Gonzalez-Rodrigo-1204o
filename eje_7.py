#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

# Función para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    
    # Comprobar si la palabra es igual a su inversa
    return palabra == palabra[::-1]

# Ejemplo de uso
palabra = input("Ingresa una palabra: ")

# Verificar si la palabra es un palíndromo
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
