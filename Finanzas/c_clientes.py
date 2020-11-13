#CLASE
class Clientes: 
#ATRIBUTOS
    def __init__ (self, nombre, identificador, saldo):
        self.nombre=nombre
        self.identificador=identificador
        self.saldo=saldo 

#METODOS:
    def init (self): 
        print("metodo init")
    def girar (self):
        print("metodo girar")
    def abonar (self):
        print("metodo abonar")
    def mostrar_saldo (self):
        print("metodo mostrar")
