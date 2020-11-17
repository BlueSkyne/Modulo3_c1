#CLASE
class Financiera:
# ATRIBUTOS    
    def __init__(self, nombre, identificador, saldo_institucional, clientes): 
        self.nombre = nombre
        self.identificador = identificador
        self.saldo_institucional = saldo_institucional
        self.clientes = []
#   METODOS:
    def agregar_cliente (self,cliente):
        if self.saldo_institucional >=  10000000:
            self.clientes.append(cliente)
            self.saldo_institucional  = self.saldo_institucional - 1000000  
            print("Felicitaciones has sido añadido a: ", self.nombre, " Cliente: ", cliente.nombre)
        else:
            print("No puedo agregarte")

        #print(str(self.saldo_institucional))
    
    
    def listar_cliente (self,):
        print(self.nombre)
       

    def eliminar_cliente (self): 
        print("eliminar_cliente") 

    def Cliente_entidad(self, clientes, nombre):
        print(self.clientes)
        print(nombre) 
        
        
    def transferir (self,desde,hacia,monto):
        if desde in self.clientes:
            
            if desde.saldo - monto < -1000000:
                print("Transferencia rechazada ya que excede su limite de credito!")
            else:
                desde.girar(monto)
                hacia.abonar(monto)
                print("Transferencia exitosa de CLP " + str(monto) + " | " + desde.nombre+ " a " + hacia.nombre)
        else:
            print("Usted no es cliente de este banco.")   


    def giros_totales (self): 
        print("giros_totales") 

    def abonos_totales (self): 
        print("abonos_totales") 

    def mostrar_saldo_institucional (self): 
        print("mostrar_saldo_institucional")         

   