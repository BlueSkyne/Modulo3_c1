def trans_entre_cliente(envia,recibe,monto):#cris
    #hacer fx que transfiera entre cliente y que valide que el cliente que envia tiene saldo
#    if envia.saldo-monto < -1000000:
    if not envia.girar(monto):
#        print(envia.nombre + "No tiene saldo suficiente!!!")
        return
    else:
        envia.girar(monto)  
        recibe.abonar(monto)
    print("Luego de la Transaccion: ")
    print(envia.nombre + " : Saldo :" + str(envia.saldo))
    print(recibe.nombre  + " : Saldo :" + str(recibe.saldo))    
    return envia, recibe, monto

def trans_cliente_ent(envia,recibe,monto):#guido
    #fx donde cliente transfiera a entidad sin sobrepasar su saldo (-1000000)
    return envia,recibe,monto


# AREA DE PRUEBAS UNITARIAS
'''
if __name__ == "__main__":
    cliente1 = Clientes("Juan0" , "1" , 5055)
    cliente2 = Clientes("juan1" , "2", 0) 
    trans_entre_cliente(cliente1,cliente2, 120000)
    pass
'''
