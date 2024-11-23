#2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.7

# Definir la función mayor3 antes de llamarla
def mayor3(a, b, c):
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    else:
        return c  

# Solicitar los números al usuario
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))


print("El mayor de los tres números es:", mayor3(a, b, c)) # Llamar a la función mayor3 con los valores ingresados y mostrar el resultado

