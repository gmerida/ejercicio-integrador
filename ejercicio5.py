
""" el siguiente metodo es interativo
    Solicita al usuario que ingrese un valor entero y lo devuelve.
    Itera mientras el valor no sea un entero válido.
"""

def get_int_iterativo():
    
    while True:
        try:
            valor = int(input("Por favor, ingrese un número entero: "))
            return valor
        except ValueError:
            print("Valor no válido. Inténtelo de nuevo.")

# Ejemplo de uso iterativo
print(" <<<Probamos metodo INTERATIVO>>> \n")
numero_iterativo = get_int_iterativo()
print(f"El número ingresado es: {numero_iterativo}")

#///////////////////////////////////////////////////////////////////////////////////////////

""" el siguiente metodo es recursivo
    Solicita al usuario que ingrese un valor entero y lo devuelve.
    Llama a sí mismo recursivamente mientras el valor no sea un entero válido.
    """
def get_int_recursivo():
    
    try:
        valor = int(input("Por favor, ingrese un número entero: "))
        return valor
    except ValueError:
        print("Valor no válido. Inténtelo de nuevo.")
        return get_int_recursivo()

# Ejemplo de uso recursivo
print(" <<< ahora Probamos metodo RECURSIVO >>> \n")
numero_recursivo = get_int_recursivo()
print(f"El número ingresado es: {numero_recursivo}")
