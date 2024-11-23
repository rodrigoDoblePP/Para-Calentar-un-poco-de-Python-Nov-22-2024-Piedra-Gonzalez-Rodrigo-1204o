#1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 

a = int(input("Ingresa el primer número: ")) # Solicitar al usuario que ingrese dos números
b = int(input("Ingresa el segundo número: "))


def mayor(a, b):  #Creamos la funcion
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a  # o return b, ya que a == b en este caso




print("El mayor numero es:", mayor(a, b)) # Llamar a la función mayor con los valores ingresados y mostrar el resultado
