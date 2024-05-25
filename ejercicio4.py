
"""
 la siguiente funcion Cuenta la frecuencia de cada palabra en una cadena de caracteres que recibe 
 como parametro la cadena de caracteres (str) donde Retorna un diccionario con cada palabra y frecuencia
 """
def contar_palabras(cadena):
    
    # Convertir la cadena a minúsculas para que el conteo sea insensible a mayúsculas/minúsculas
    cadena = cadena.lower()
    
    # Reemplazar los signos de puntuación por espacios (opcional, para mejor separación de palabras)
    import string
    for char in string.punctuation:
        cadena = cadena.replace(char, " ")
    
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Contar la frecuencia de cada palabra
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia


"""
  La siguiente funcion encuentra la palabra mas repetida y su frecuencia , doma parametros a analizar 
  de un diccionario  frecuencia_palabras (dict) , devuelve una tupla con la palabra mas repetida y frecuencia.
"""
def palabra_mas_repetida(frecuencia_palabras):
    
    if not frecuencia_palabras:
        return None, 0
    
    palabra_max = max(frecuencia_palabras, key=frecuencia_palabras.get)
    frecuencia_max = frecuencia_palabras[palabra_max]
    
    return palabra_max, frecuencia_max


# Ejemplo de aplicacion 
cadena = input('ingrese la ORACION para medir su frecuencia\n ')
frecuencia_palabras = contar_palabras(cadena)
print(frecuencia_palabras)

palabra, frecuencia = palabra_mas_repetida(frecuencia_palabras)
print(f"La palabra más repetida es '{palabra}' con una frecuencia de {frecuencia}.")
