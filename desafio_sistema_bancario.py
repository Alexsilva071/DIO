#DESAFIO SISTEMA BANCÁRIO
saldo=300
LIMITE_DE_SAQUE=3
numero_de_saque=0
limite=500


checagem=-1
while checagem!=4:
    checagem = int(input("Pressione [1]para depositar, pressione [2] para sacar, pressione [3] para extrato,pressione [4]para sair "))
#DEPOSITO
    if checagem ==1:

        deposito = float(input("Insira aqui o valor para deposito "))
        saldo+=deposito
        print(f"você depositou o valor de R${deposito}, seu saldo agora é de R${saldo}")
   #SAQUE
    elif checagem ==2:
        saque = float(input("Insira aqui o valor para saque "))
         
        if saque>saldo:
                print(f2
                "Não é possivel realizar essa operação por falta de saldo. Seu saldo é de: {saldo}.")
                break    
        if saque > 500:
             print("Seu limite para saque é de R$ 500,00")
             break
     
        
        saldo-=saque
        
        print(f"você sacou o valor de R${saque}, seu saldo agora é de R${saldo}")
        numero_de_saque+=1
        if LIMITE_DE_SAQUE==numero_de_saque:
            print("Você atingiu seu limite diário de saques.") 
            break
  #EXTRATO      
    elif checagem ==3:
        print(f"seu saldo é de {saldo}")
   
   #SAIR

    elif checagem ==4:
        print ("Obrigado por usar nossos serviços.")
        break