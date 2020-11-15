#CLASE
class Financiera:
# ATRIBUTOS    
    def __init__(self, nombre, identificador, saldo_institucional, clientes): 
        self.nombre = nombre
        self.identificador = identificador
        self.saldo_institucional = saldo_institucional
        self.clientes = clientes
#   METODOS:
    def agregar_cliente (self,cliente):
        self.clientes.append(cliente)
        #print("agregar_cliente") 
    
    def listar_cliente (self):
        print(self.nombre)

    def eliminar_cliente (self): 
        print("eliminar_cliente") 

    def transferir (self,desde,hacia,monto):
        if desde.saldo - monto < -1000000:
            print("Transferencia rechazada ya que excede su limite de credito!")
        else:
            desde.girar(monto)
            hacia.abonar(monto)
            print("Transferencia exitosa de CLP " + str(monto) + " | " + desde.nombre+ " a " + hacia.nombre)

    def giros_totales (self): 
        print("giros_totales") 

    def abonos_totales (self): 
        print("abonos_totales") 

    def mostrar_saldo_institucional (self): 
        print("mostrar_saldo_institucional")         

   