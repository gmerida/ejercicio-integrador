
"""  La siguiente funcion calcula el MCD entre dos numeros enteros y devuelve un entero """
def calcular_mcd(a, b):

    while b != 0:
        a, b = b, a % b
    return a

# aplicamos funcion
num1 = int(input('ingrese por teclado el primer numero-->' ))
num2 = int(input('ingrese por teclado el segundo numero-->' ))
print(f"El MCD de {num1} y {num2} es >>> {calcular_mcd(num1, num2)}")

