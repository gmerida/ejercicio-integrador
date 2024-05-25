"""
  la siguiente funcion Cuenta la frecuencia de cada palabra en una cadena de caracteres que recibe 
 como parametro la cadena de caracteres (str) donde Retorna un diccionario con cada palabra y frecuencia
 """

def contar_palabras(cadena):
    
    #convierte la cadena a minúsculas para que el conteo sea insensible a mayúsculas/minúsculas
    cadena = cadena.lower() 
    
    # Reemplazar los signos de puntuación por espacios (opcional, para mejor separación de palabras)
    import string
    for char in string.punctuation:
        cadena = cadena.replace(char, " ") 
    
    # Dividir la oracion en cadena de palabras 
    palabras = cadena.split()
    #print(palabras)
    
    # Contar la frecuencia de cada palabra
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

# Ejemplo de aplicacion 
cadena = input('ingrese la ORACION para medir su frecuencia\n ')
frecuencia_palabras = contar_palabras(cadena)
print(frecuencia_palabras)
