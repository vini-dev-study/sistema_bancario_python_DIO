menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    if opcao == 'd':
        valor = float(input('Digite o valor a ser depositado: \n'))
        saldo += valor
        extrato.append(f'Depósito: R$ {valor:.2f}')
    elif opcao == 's':
        if numero_saques < limite_saques:
            valor = float(input('Digite o valor a ser sacado: \n'))
            
            if valor > limite:
                print('\nValor de saque acima do limite diário.')
            elif saldo >= valor:
                saldo -= valor
                extrato.append(f'Saque: R$ {valor:.2f}')
                numero_saques += 1
            else:
                print('Saldo insuficiente.')
        else:
            print('Limite de saques atingido.')
    elif opcao == 'e':
        print(f'Saldo: R$ {saldo:.2f} \n')
        print('Extrato:')
        for operacao in extrato:
            print(operacao)
    elif opcao == 'q':
        break
    else:
        print('Opção inválida.')