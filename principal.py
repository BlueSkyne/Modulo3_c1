import Finanzas as f
import uuid
import random

#punto 1 de tarea 2 entidades con nombre y saldo inicial de 100000000
print("ENTIDADES CREADAS...")
entidad1 = f.Financiera("Banco Estado", uuid.uuid4() ,100000000,[])
#print(entidad1)
entidad2 = f.Financiera("Banco BCI", uuid.uuid4() ,100000000,[])
#print(entidad2)

print()
print("CLIENTES CREADOS...")
cliente1 = f.Clientes("Juan1" , uuid.uuid4(), 1000)
cliente2 = f.Clientes("juan2" , uuid.uuid4(), 2000)
cliente3 = f.Clientes("Juan3" , uuid.uuid4(), 3000)
cliente4 = f.Clientes("Juan4" , uuid.uuid4(), 40000000)
cliente5 = f.Clientes("Juan5" , uuid.uuid4(), 50000000)
cliente6 = f.Clientes("Juan6" , uuid.uuid4(), 6000)
cliente7 = f.Clientes("Juan7" , uuid.uuid4(), 7000)
cliente8 = f.Clientes("Juan8" , uuid.uuid4(), 8000)

print()
print("ASIGNANDO CLIENTES A ENTIDADES FINANCIERAS...")
#ASIGNACION DE CLIENTES A ENTIDAD1
entidad1.agregar_cliente(cliente1)
entidad1.agregar_cliente(cliente2)
entidad1.agregar_cliente(cliente3)
entidad1.agregar_cliente(cliente4)

#ASIGNACION DE CLIENTES A ENTIDAD2
entidad2.agregar_cliente(cliente5)
entidad2.agregar_cliente(cliente6)
entidad2.agregar_cliente(cliente7)
entidad2.agregar_cliente(cliente8)

#pto 3 tarea trans_entre_cliente
print()
print("TRANSACCIONES ENTRE CLIENTES (24):")
lista_clientes_global = entidad1.clientes + entidad2.clientes   
print(lista_clientes_global)
f.transf_aleat(12, entidad1, lista_clientes_global)
f.transf_aleat(12, entidad2, lista_clientes_global)

#pto 4 giro entre 2 clientes en los cuales la transaccion falle por falta de saldo
print()
print("TRANSACCIONES FALLIDAS POR FALTA DE SALDO:")
print("Saldo de cliente que pretende enviar: " + str(cliente1.saldo) + " Saldo de cliente que debe recibir: " + str(cliente2.saldo))
entidad1.transferir(cliente1, cliente2, 10000000)
print("Saldo de cliente que pretendia enviar: " + str(cliente1.saldo) + " Saldo de cliente que debe recibir: " + str(cliente2.saldo))
print()
print("Saldo de cliente que pretende enviar: " + str(cliente6.saldo) + " Saldo de cliente que debe recibir: " + str(cliente1.saldo))
entidad2.transferir(cliente6, cliente1, 100000000)
print("Saldo de cliente que pretendia enviar: " + str(cliente6.saldo) + " Saldo de cliente que debe recibir: " + str(cliente1.saldo))

#pto 5 realizar 4 transferencias entre clientes 
print()
print("4 TRANSACCIONES ENTRE CLIENTES:")
f.transf_aleat(2, entidad1, lista_clientes_global)
f.transf_aleat(2, entidad2, lista_clientes_global)

#pto 6 realizar 2 transferecias entre cliente y financiera (guido)
print()
print("2 TRANSACCIONES ENTRE CLIENTES Y FINANCIERAS:")
print("Saldo de cliente que pretende enviar: " + str(cliente4.saldo) + " Saldo de Financiera que recibira: " + str(entidad1.saldo_institucional))
entidad1.tr_cliente_financiera(cliente4,200000)
print("Saldo de cliente: " + str(cliente4.saldo) + " Saldo de Financiera: " + str(entidad1.saldo_institucional))
print("Saldo de cliente que pretende enviar: " + str(cliente7.saldo) + " Saldo de Financiera que recibira: " + str(entidad2.saldo_institucional))
entidad2.tr_cliente_financiera(cliente7,100000)
print("Saldo de cliente: " + str(cliente7.saldo) + " Saldo de Financiera: " + str(entidad2.saldo_institucional))

#pto 7 son similares preguntar al respecto
print()
print("2 TRANSACCIONES ENTRE CLIENTES Y FINANCIERAS QUE DEMUESTRE QUE SALDO DE CLIENTE NO PUEDE SER MENOR A -1000000:")
print("Saldo de cliente que pretende enviar: " + str(cliente3.saldo) + " Saldo de Financiera que recibira: " + str(entidad1.saldo_institucional))
entidad1.tr_cliente_financiera(cliente3,100000)
print("Saldo de cliente: " + str(cliente7.saldo) + " Saldo de Financiera: " + str(entidad2.saldo_institucional))
print("Saldo de cliente que pretende enviar: " + str(cliente7.saldo) + " Saldo de Financiera que recibira: " + str(entidad2.saldo_institucional))
entidad2.tr_cliente_financiera(cliente8,100000)
print("Saldo de cliente: " + str(cliente8.saldo) + " Saldo de Financiera: " + str(entidad2.saldo_institucional))

#pto 8 y 9 preguntar por la cosa del 10%
print()
print("2 TRANSACCIONES ENTRE CLIENTES Y FINANCIERAS QUE DEMUESTRE QUE SALDO DE CLIENTE NO PUEDE SER MENOR A -1000000:")

print("Saldo de cliente que pretende enviar: " + str(cliente4.saldo) + " Saldo de cliente que debe recibir: " + str(cliente2.saldo))
entidad1.transferir(cliente4, cliente2, 10000000)
print("Saldo de cliente que pretendia enviar: " + str(cliente4.saldo) + " Saldo de cliente que debe recibir: " + str(cliente2.saldo))
print()
print("Saldo de cliente que pretende enviar: " + str(cliente5.saldo) + " Saldo de cliente que debe recibir: " + str(cliente1.saldo))
entidad2.transferir(cliente5, cliente1, 12000000)
print("Saldo de cliente que pretendia enviar: " + str(cliente5.saldo) + " Saldo de cliente que debe recibir: " + str(cliente1.saldo))

#pto 9 Demostrar que su código no puede agregar clientes en casos en que el límite de 10% del saldo institucional se viole.
#Para este caso generamos una entidad 3
print("ENTIDAD CREADA...")
entidad3 = f.Financiera("Banco Falabela", uuid.uuid4() ,12000000,[])
print("CLIENTES CREADOS...")
cliente09 = f.Clientes("Pepe1" , uuid.uuid4(), 1000)
cliente10 = f.Clientes("Pepe2" , uuid.uuid4(), 2000)
cliente11 = f.Clientes("Pepe3" , uuid.uuid4(), 3000)
cliente12 = f.Clientes("Pepe4" , uuid.uuid4(), 3000)
print("ASIGNANDO CLIENTES A ENTIDADES FINANCIERAS...")
#ASIGNACION DE CLIENTES A ENTIDAD3
entidad3.agregar_cliente(cliente09)
entidad3.agregar_cliente(cliente10)
entidad3.agregar_cliente(cliente11)
entidad3.agregar_cliente(cliente12)

#pto 10 imprimir estado cuentas como tablas (pto 11) 
print("******* EDC CLIENTES *******")
cliente1.edc()
print()
cliente2.edc()
print()
cliente3.edc()
print()
cliente4.edc()
print()
cliente5.edc()
print()
cliente6.edc()
print()
cliente7.edc()
print()
cliente8.edc()
print()
print("######## EDC ENTIDADES ########")
entidad1.edc()
print()
entidad2.edc()
print()
