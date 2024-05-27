import os

menu = """
[d] Depósitar
[s] Sacar
[e] Extratro
[a] Sair
\n
\n
"""

saldo = 0 
limite = 500
extrato = ""
QtdSaques = 0 
LimiteSaques = 3 

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor e invalido para depósito.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))

        SaldoExcedido = saldo < valor

        LimiteSaque = limite < valor

        LimiteQtdeSaque = QtdSaques >= LimiteSaques

        if SaldoExcedido:
            print("Operação Falhou! Valor desejado maior que saque! Tente novamente.")
        
        elif LimiteSaques: 
            print("Operação Falhou! Valor exedeu o limite do valor para saque!")
        
        elif LimiteQtdeSaque:
            print("Operação Falhou! Quantidade de saques exedida para hoje! Tente novamente amanha")
        
        elif valor > 0 :
            saldo -= valor  
            extrato += f"Saque: R$ {valor:.2f}\n"
            QtdSaques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n====================EXTRATO====================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===============================================\n")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválidade, por favor selecione novamente a opção desejada.")