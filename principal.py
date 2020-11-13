import Finanzas as f
import uuid

u = uuid.uuid4
print(u)
entidad1 = f.financiera("Carlos","001","100000000",[])
entidad2 = f.financiera("Julio","002","100000000",[])
print(entidad1.nombre)
print(entidad2.nombre)


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
