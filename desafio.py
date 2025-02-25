menu = """
    Menu Inicial

    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair

    Digite o código da operação a ser realizada
    => """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito(apenas números ex: 100 ou 100.00):\n"))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
            print(f"\nDepósito de R$ {valor_deposito:.2f} realizado com sucesso\n\n")
        else:
            print("\nOperação falhou. Digite um valor válido.\n\n####################\n\nRetornando ao Menu Principal...\n\n")

    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque(apenas números ex: 100 ou 100.00):\n"))
        if numero_saques < 3:
            if valor_saque > 0:
                if valor_saque > 500:
                    print("\nValor de saque acima do permitido. Tente novamente.\nValor máximo por saque: R$ 500.00\n\n")
                else:
                    if saldo >= valor_saque:
                        saldo -= valor_saque
                        extrato += f"Saque de R$ {valor_saque:.2f}\n"
                        numero_saques += 1
                        print(f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso. Saques diários restantes: {LIMITE_SAQUES - numero_saques}\n\n")

                    else:
                        print("\nSaldo insuficiente.\n\n")
            else:
                print("\nOperação falhou. Digite um valor válido.\n\n####################\n\nRetornando ao Menu Principal...\n\n")
        else:
            print("\nNúmero limite de saques diário atingido. Tente novamente outro dia.\n\n")

    elif opcao == "e":
        print(" Extrato da conta ".center(30,"#"))
        print(f"{extrato}\n\nSaldo final: R$ {saldo:.2f}\n\n")
        
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione a operação desejada.")