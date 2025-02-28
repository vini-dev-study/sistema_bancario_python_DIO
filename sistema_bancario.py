menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

numero_limite_saque = 3
numero_saque = 0
valor_limite_saque = 500
saldo = 0
extrato = []

def depositar():
    global extrato
    global saldo

    valor = float(input('Qual valor deseja depositar?'))
    saldo += valor
    extrato.append(f"Deposito no valor de R$ {valor:.2f}")


def sacar():
    global valor_limite_saque
    global saldo
    global extrato

    valor = float(input('Qual valor deseja sacar?'))

    if valor > valor_limite_saque:
        print(f'O valor R$ {valor:.2f} está acima do limite diário de R$ {valor_limite_saque:.2f}')
    elif saldo >= valor:
        saldo -= valor
        extrato.append(f"Saque no valor de R$ {valor:.2f}")

    else:
        print("Saldo insuficiente!")
    
while True:
    opcao = input(menu)

    if opcao == 'd':
        depositar()
    elif opcao == 's':
        if numero_saque < numero_limite_saque:
            sacar()
            numero_saque += 1
        else:
            print('Limite de saque atingido!')
    elif opcao == 'e':
        print(f'O saldo é de: R$ {saldo:.2f} \n')
        print('Extrato: \n')

        for operacao in extrato:
            print(operacao)
    elif opcao == 'q':
        break
    else:
        print('Opção inválida. Tente novamente!')