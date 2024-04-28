'''Desafio banco, apenas um usuario, nao tem necessidade de identificar o mesmo, precisa ter Deposito, Saque e Extrato, 

DEPOSITO: Deve ser possivel depositar apenas valores inteiros e positivos, cada deposito deve ser armazenado em uma variavel e sera exibido na operação extrato.

SAQUE: O sistema deve permitir apenas 3 saques diários com limite de 500 por saque, caso nao haja saldo em conta, o sistema deve exibir que nao e possivel por falta de saldo,
todos os saques devem ser armazenados em uma variavel e exibidos na operação extrato

EXTRATO: Operação deve listar todos os depositos e saques da conta. No fim da listagem exibir o saldo atual da conta. Exemplo R$xxxx.xx'''

menu = """
-----------------------------------
[1] Depositar
[2] Sacar
[3] Extrato
[S] Sair
-----------------------------------
-> """

saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
limite = 500

while True:
    opcao = (input(menu))

    if opcao == "1":
        print("""-----------------------------------
             Deposito
-----------------------------------""")
        Valor_dep = float(input("Qual o valor do deposito? R$"))
        if Valor_dep > 0:
            saldo += Valor_dep
        prox = (input("""-----------------------------------
Algo Mais?
[1]Sim
[2]Não
-----------------------------------
-> """))
        if prox == "1":
            print(opcao)
        else:
            print("Obrigado por usar o banco Abublublé");break

    elif opcao == "2":
        print("""-----------------------------------
               Saque
-----------------------------------""")
        valor_saque = float(input("Qual o valor do saque? R$"))
        saldo -= valor_saque
        limite -= valor_saque
        if valor_saque < saldo:
            if limite < 0:
                if numero_saques == 3:
                    print("Você atingiu seus saques diarios"); break
                print("Seu limite de saques diário é de R$500.00") ; break
            print("Retire o valor na boca do caixa!")       
        else:
            print("Saldo insuficiente!")
        numero_saques += 1
        

    elif opcao == "3":
        print("""-----------------------------------
             Extrato
-----------------------------------""")
        (print(f"Seu saldo é de: R${saldo}"))
        (print(f"Você executou: {numero_saques} Saques"))
        (print(f"Você ainda pode sacar: R${limite}"))
        print("-----------------------------------")

    elif opcao == "S" or "s":
        break

    else:
        print("Selecione uma opção válida!")