#CLASE
class Clientes: 
#ATRIBUTOS
    
#METODOS:
    def __init__ (self, nombre, identificador, saldo):
        self.nombre=nombre
        self.identificador=identificador
        self.saldo=saldo 

    def girar (self,monto):
            self.saldo = self.saldo - monto

    def abonar (self,monto):
        self.saldo = self.saldo + monto

    def mostrar_saldo (self):
        return self.saldo
