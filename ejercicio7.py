"""
 Constructor de la clase Cuenta. Los datos pueden estar vacíos. 
 Parámetros:
 titular (str): Nombre de la persona. (campo obligatorio)
 cantidad (int): cuenta de la persona.(campo opcional)
 imprime en rojo al final
 """

class Cuenta:
    def __init__(self, titular):
        self.__titular = titular
        self.__cantidad = 0 

    # Getter para titular
    def get_titular(self):
        return self.__titular

    # Setter para titular
    def set_titular(self, titular):
        self.__titular = titular

    # Getter para cantidad
    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print("Titular es:", self.__titular)
        print("Cantidad actual en cuenta es:", self.__cantidad) 
        
    def mostrar_rojo(self):
        print("\n\n >> Titular es: ", self.__titular)
        print("\033[0;31;40m"+ " >> Cantidad actual en su cuenta es:", self.__cantidad) # imprime rojo
        print("\n\n ")
        
    def ingresar(self, cantidad):
    
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad

# Ejemplo de uso
if __name__ == "__main__":
    cuenta = Cuenta("Juan")
    cuenta.mostrar()  # Muestra los datos de la cuenta
    cuenta.ingresar(int(input('ingresar monto a depositar --> ')))# ingresar monto a depositar por teclado 
    cuenta.retirar(int(input('ingresar monto a retirar  --> ')))  # ingresar monto a retirar por teclado 
    cuenta.mostrar_rojo()  # Muestra los datos actualizados de la cuenta
    