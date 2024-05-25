"""
  Constructor de la clase Cuenta. Los datos pueden estar vacíos. 
 Parámetros:
 titular (str): Nombre de la persona. 
 cantidad (int): cuenta de la persona.
 imprime en rojo al final
 """

class Cuenta:
    def __init__(self, titular='', cantidad=0.0):
     self._titular = titular
     self._cantidad = cantidad

    # Getters y Setters para titular
    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    # Getters y Setters para cantidad
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

class CuentaJoven(Cuenta):
    def __init__(self, titular='', cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion

    # Getters y Setters para bonificación
    @property
    def bonificacion(self):
        return self._bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self._bonificacion = bonificacion

    def es_titular_valido(self, edad):
        print("\n***La edad  es:", edad,"años")
        return 18 <= edad < 25

    def retirar(self, retiro, edad):
        
        if self.es_titular_valido(edad):
            saldoActual=self.cantidad + 100/self.bonificacion
            if retiro <= saldoActual:
                saldoActual -= retiro
                return f"***Retiraste {retiro} Pesos. \n***Si retiraste tu Saldo actual es: {saldoActual} $$$."
            else:
                return "No tienes saldo para retirar esa cantidad."
        else:
            return "El titular no es válido para realizar el RETIRO."

    def mostrar(self):
        print(" *** cantidad actual es: >>>", self.cantidad)
        print(" *** bonificaciones  es: >>>", self.bonificacion,"%")
        print(" *** cantidad total con Bonificacion es: >>>", self.cantidad + 100/self.bonificacion)
        #return f"Cuenta Joven con una bonificación del {self.bonificacion}%"

# Ejemplo de uso
cuenta_joven = CuentaJoven('Juan', 1000, 10)# indico que se llama juan y saldo actual 1000$ y bonificacion
print(cuenta_joven.mostrar())  # Muestra todo saldo actual + bono y total
print(cuenta_joven.retirar(100, 20))  # Realiza retiro de 100$ e impongo edad 20 años si el titular es válido y muestra el saldo actual

