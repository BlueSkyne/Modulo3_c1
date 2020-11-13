#CLASE
class Clientes: 
#ATRIBUTOS
    
#METODOS:
    def __init__ (self, nombre, identificador, saldo):
        self.nombre=nombre
        self.identificador=identificador
        self.saldo=saldo 

    def girar (self,monto):
        if self.saldo - monto < -1000000:
            print("No tiene suficiente saldo.")
        else:
            self.saldo = self.saldo - monto

    def abonar (self,monto):
        self.saldo = self.saldo + monto
        #print("metodo abonar")

    def mostrar_saldo (self):
        return self.saldo
