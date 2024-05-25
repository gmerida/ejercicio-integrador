

""" La siguiente funcion calcula el MCD entre dos numeros enteros y devuelve un entero """
def calcular_mcd(a, b):
    
    while b != 0:
        a, b = b, a % b
    return a

""" La siguiente funcion calcula el MCM entre dos numeros enteros y devuelve un entero """
def calcular_mcm(a, b):
   
    mcd = calcular_mcd(a, b)
    return abs(a * b) // mcd

# Ejemplo de aplicacion 

num1 = int(input('ingrese por teclado el primer numero-->' ))
num2 = int(input('ingrese por teclado el segundo numero-->' ))
# num1 = 48
# num2 = 18
print(f"El MCM de {num1} y {num2} es >>>>  {calcular_mcm(num1, num2)}")
