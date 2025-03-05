import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


valor_limite_saque = 500
saldo = 0
extrato = []
numero_transacao = 0
limite_transacao = 10



def depositar():
    global extrato
    global saldo
   

    valor = float(input('Qual valor deseja depositar? '))
    saldo += valor
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y ás %H:%M")

    extrato.append(f"Depósito realizado no valor de R$ {valor:.2f} no dia {data_atual}")


def sacar():
    global valor_limite_saque
    global saldo
    global extrato

    valor = float(input('Qual valor deseja sacar? '))

    if valor > valor_limite_saque:
        print(f'O valor R$ {valor:.2f} está acima do limite diário de R$ {valor_limite_saque:.2f}')
    elif saldo >= valor:
        saldo -= valor
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y ás %H:%M")

        extrato.append(f"Saque realizado no valor de R$ {valor:.2f} no dia {data_atual}")

    else:
        print("Saldo insuficiente!")
    
while True:
    opcao = input(menu)

    if opcao == 'd':
        if numero_transacao < limite_transacao:
            numero_transacao += 1
            depositar()
        else:
            print('Número de transações diárias foi excedido!')
    elif opcao == 's':
        if numero_transacao < limite_transacao:
            sacar()
            numero_transacao += 1
        else:
            print('Número de transações diárias foi excedido!')
    elif opcao == 'e':
        print(f'O saldo é de: R$ {saldo:.2f} \n')
        print('Extrato: \n')

        for operacao in extrato:
            print(operacao)
    elif opcao == 'q':
        break
    else:
        print('Opção inválida. Tente novamente!')