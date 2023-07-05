menu="""
[d]Depósito
[s]Saque
[e]Extrato
[q]Sair"""

saldo=0
LIMITE_DE_SAQUE=3
numero_de_saque=0
extrato=""
limite=500

while menu == True:

    opcao=input(menu)
    
    if opcao=="d":
        print("Depósito")
    elif opcao=="s":
        print("Saque")
    elif opcao=="e":
        print("Extrato")
    elif opcao=="q":
        break
    else: 
        print("Opção Inválida, seleciona uma opção válida.")








         if checagem ==1:

        deposito = float(input("Insira aqui o valor para deposito "))
        saldo+=deposito
        print(f"você depositou o valor de R${deposito}, seu saldo agora é de R${saldo}")
    if checagem ==2:
        saque = float(input("Insira aqui o valor para saque "))
        saldo-=saque
        print(f"você sacou o valor de R${saque}, seu saldo agora é de R${saldo}")
    else:
        print(f"seu saldo é de {saldo}")
