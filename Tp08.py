"""#Ejercicio 1 
def contar_digitos(n):
    # Convierte el número a una cadena para contar los dígitos
    num_str = str(n)
    # Usa la función len() para contar la longitud de la cadena
    cantidad_de_digitos = len(num_str)
    return cantidad_de_digitos

# Ejemplo de uso
numero = int(input("Ingrese un numero entero positivo: "))
resultado = contar_digitos(numero)
print(f"El número {numero} tiene {resultado} dígitos.")

#Ejercicio 2
def es_potencia(n, b):
    if n == 1:
        return True  # Cualquier número elevado a la potencia 0 es 1
    if n < 1 or b < 1:
        return False  # No se admiten números no positivos

    exponente = 0
    resultado = 1
    while resultado < n:
        resultado = b ** exponente
        exponente += 1

    return resultado == n

# Ejemplo de uso
n = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
resultado = es_potencia(n, b)
if resultado:
    print(f"{n} es potencia de {b}.")
else:
    print(f"{n} no es potencia de {b}.")"""

#Ejercicio 3
