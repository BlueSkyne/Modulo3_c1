import Finanzas as f
import uuid

"""
while:
    print("Menú: ")
    if salir:
        break
    elif entidad:
        #crear entidades
    elif cliente:
        #crear cliente
    elif transferencia_cliente:
        #trans cliente
    elif trans_cliente_financiera:
    
    elif imprimir_estado_c_cliente

    elif imp_est_c_financiera:
#imprimir tabla

"""


    

    

#ID Revisar
u = uuid.uuid4
print("este es el uuid", u)

#entidades
entidad1 = f.Financiera("Banco Estado", u ,"100000000",[])
u = uuid.uuid4
print("este es el uuid", u)
entidad2 = f.Financiera("Banco BCI", u ,"100000000",[])
u = uuid.uuid4
print("este es el uuid", u)
#clientes
cliente1 = f.Clientes("Juan" , uuid.uuid4 , 5055)
cliente1.girar( 2000000 )
#cliente1.saldo( )
"""

cliente2 = f.Clientes("juan1" , uuid.uuid4, 0)
cliente3 = f.Clientes("Juan2" , uuid.uuid4, 0)
cliente4 = f.Clientes("Juan3" , uuid.uuid4, 0)
cliente5 = f.Clientes("Juan4" , uuid.uuid4, 0)
cliente6 = f.Clientes("Juan5" , uuid.uuid4, 0)
cliente7 = f.Clientes("Juan6" , uuid.uuid4, 0)
cliente8 = f.Clientes("Juan7" , uuid.uuid4, 0)




print(entidad1.nombre)
print(entidad2.nombre)

print(cliente1.nombre + " " + str(cliente1.saldo) , " " , str(cliente1.identificador))
print(cliente2.nombre + " " + str(cliente2.saldo) + " " + str(cliente2.identificador))
print(cliente3.nombre + " " +  str(cliente3.saldo))
print(cliente4.nombre + str(cliente4.saldo))
print(cliente5.nombre + str(cliente5.saldo))
print(cliente6.nombre + str(cliente6.saldo))
print(cliente7.nombre + str(cliente7.saldo))
print(cliente8.nombre + str(cliente8.saldo))

print(cliente1.saldo + cliente2.saldo)

# Mecánica para operación de líneas de crédito.
# considerar línea de crédito un saldo negativo cubierto por el saldo_institucional y de $1Millón por cliente
# El límite máximo asignado a líneas de crédito no puede superar el 10% del saldo_institucional
#     Esto limita la cantidad de clientes y el monto disponible para transferencias desde el saldo_instritucional
# El método agregar_cliente debe verificar que se cumple la condición del 10%, de lo contrario rechazar la creación
# El método transferir debe verificar que el saldo_institucional satisfaga la condición del 10%, de lo contrario rechazar la transferencia.
# El método transferir debe permitir transferencias clientes-clientes y clientes-financiera
# Los id de clientes y financieras deberán ser creados con el módulo uuid y utilizando uuid4().
# Las clases mencionadas deberán estar implementadas en un módulo llamado finanzas.
#Deberá crear un script principal que importe el módulo finanzas.
"""