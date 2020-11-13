def trans_entre_cliente(envia,recibe,monto):#cris
    #hacer fx que transfiera entre cliente y que valide que el cliente que envia tiene saldo
     if envia.saldo-monto < -1000000:
         print("ud. no tiene saldo")
     else:
         envia.girar(monto)  
         abonar.recibe(monto)
     print(envia.nombre + "" + str(mostrar_saldo_institucional))
     print(recibe.nombre  + "" + str(mostrar_saldo_institucional))    
          
#return envia, cliente_recibe
    


def trans_cliente_ent(envia,recibe,monto):#guido
    #fx donde cliente transfiera a entidad sin sobrepasar su saldo (-1000000)


    return envia,cliente_recibe


if __name__ == "__main__":
    cliente1 = f.Clientes("Juan0" , "1" , 5055)
    cliente2 = f.Clientes("juan1" , "2", 0) 

    trans_entre_cliente(cliente1,cliente2, 120000)
    
    pass

