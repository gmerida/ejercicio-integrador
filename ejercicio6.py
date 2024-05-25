"""
 Constructor de la clase Persona. Los datos pueden estar vacíos. 
 Parámetros:
 nombre (str): Nombre de la persona.
 edad (int): Edad de la persona.
 dni (str): DNI de la persona.
 """
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    # Getters
    def get_nombre(self):
        return self._nombre
    
    def get_edad(self):
        return self._edad

    def get_dni(self):
        return self._dni
    
    # Setters
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía.")
    
    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un número entero no negativo.")
    
    def set_dni(self, dni):
        if isinstance(dni, str) and dni.strip():
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena no vacía.")
    
    # Método para mostrar los datos de la persona
    def mostrar(self):
        print('*   ')
        print(f"*  Nombre: {self.get_nombre()}")
        print(f"*  Edad: {self.get_edad()}")
        print(f"*  DNI: {self.get_dni()}")
       
    # Método para verificar si la persona es mayor de edad
    def es_mayor_de_edad(self):
        """
        Devuelve un valor lógico indicando si es mayor de edad.
        Retorna:
        bool: True si la edad es 18 o más, False en caso contrario.
        """
        return self.get_edad() >= 18

# Ejemplo de uso
persona = Persona()
persona.set_nombre(input('Ingrese el nombre: \n' ))
persona.set_edad(int(input( 'ingrese la edad: \n')))
persona.set_dni(input( 'ingrese la dni: \n'))

print('\n\n\n\n\n')
print('*********************USTED INGRESO LOS SIGUIENTES DATOS *******************************')
persona.mostrar()
print(f"*  Es mayor de edad?: {persona.es_mayor_de_edad()}")
print('*   ')
print('***************************************************************************************')
