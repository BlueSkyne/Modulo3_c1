#CLASE
class Financiera:
# ATRIBUTOS    
    def __init__(self, nombre, identificador, saldo_institucional, clientes): 
        self.nombre=nombre
        self.identificador=identificador
        self.saldo_institucional=saldo_institucional
        self.clientes=clientes
#   METODOS:
    def init (self): 
        print("metodo init")

    def agregar_cliente (self,cliente):
        self.clientes.append(cliente)
      #print("agregar_cliente") 
    
    def listar_cliente (self):
        print(self.cliente)

    def eliminar_cliente (self): 
        print("eliminar_cliente") 

    def transferir (self): 
        print("transferir") 

    def giros_totales (self): 
        print("giros_totales") 

    def abonos_totales (self): 
        print("abonos_totales") 

    def mostrar_saldo_institucional (self): 
        print("mostrar_saldo_institucional")         

   