menu = """
    Menu Inicial

    [c] - Cadastrar Usuário
    [cc] - Criar Conta Corrente
    [lu] - Listar Usuários
    [lc] - Listar Contas
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
numero_transacoes = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
numero_conta = 1

lista_contas = []

lista_clientes = {
}

def cadastrar_usuario(lista_clientes):
    cpf = input('Digite o seu CPF(apenas números):\n')
    if cpf in lista_clientes:
        print("CPF informado já possui cadastro.")
        return None
    else:
        nome = input("Digite seu nome:\n")
        data_nascimento = input("Digite a data do seu nascimento no formato DD/MM/YYYY::\n")
        endereco = input("Digite seu endereço no formato Logradouro, numero - Bairro - Cidade/Sigla do Estado:\n")

        lista_clientes.update({cpf : {'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco}})
        
        print("#" * 30)
        print("\nCliente Cadastrado com Sucesso!\n")
        return lista_clientes

def criar_conta(lista_contas, numero_conta, lista_clientes):
    cpf = input("Digite o seu CPF(apenas números):\n")
    if cpf in lista_clientes:
        usuario = lista_clientes[cpf]['nome']
        nova_conta = {
            'cpf' : cpf,
            'nome': usuario,
            'agencia' : '0001',
            'conta' : numero_conta
        }

        lista_contas.append(nova_conta)
        
        print("#" * 30)
        print("\nConta Corrente criada com Sucesso!\n")
        return lista_contas
    else:
        print("CPF não encontrado. Tente novamente e digite um CPF que já possua cadastro para criar uma Conta Corrente.\n Voltando ao Menu Inicial...")
        return None
    

def listar_clientes(lista_clientes):
    print('\n\n\n')
    print(" Lista de Clientes ".center(50,"#"))
    for cpf, cliente in lista_clientes.items():
        linha = f"""
            Nome: {cliente['nome']}
            CPF: {cpf}
            Data de Nascimento: {cliente['data_nascimento']}
            Endereço: {cliente['endereco']}
        
        """
        print("#" * 50)
        print(linha)
    
    print('\n\n\n')

def listar_contas(lista_contas, lista_clientes):
    print('\n\n\n')
    print(" Lista de Contas ".center(50,"#"))

    for conta in lista_contas:
        linha = f"""
            Agência: {conta['agencia']}
            Nome: {conta['nome']}
            CPF: {conta['cpf']}
            Conta: {conta['conta']}
        """
        print("#" * 50)
        print(linha)
    print('\n\n\n')

def sacar(*, valor_saque, saldo, extrato, numero_transacoes, numero_saques):
    if numero_transacoes < 10:
        if numero_saques < 3:
                if valor_saque > 0:
                    if valor_saque > 500:
                        print("\nValor de saque acima do permitido. Tente novamente.\nValor máximo por saque: R$ 500.00\n\n")
                    else:
                        if saldo >= valor_saque:
                            saldo -= valor_saque
                            extrato += f"Saque de R$ {valor_saque:.2f}\n"
                            numero_saques += 1
                            numero_transacoes += 1
                            print(f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso. Saques diários restantes: {LIMITE_SAQUES - numero_saques}. Transações diárias restantes: {LIMITE_TRANSACOES - numero_transacoes}\n\n")

                        else:
                            print("\nSaldo insuficiente.\n\n")
                else:
                    print("\nOperação falhou. Digite um valor válido.\n\n####################\n\nRetornando ao Menu Principal...\n\n")
        else:
            print("\nLimite de saques diários atingido. Tente novamente outro dia.\n\n")
    else:
        print("\nLimite de transações diárias atingido. Tente novamente outro dia.\n\n ")

    return saldo, extrato, numero_saques, numero_transacoes


def depositar(valor_deposito, saldo, extrato, numero_transacoes, /):
    if numero_transacoes < 10:
        if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
                numero_transacoes += 1
                print(f"\nDepósito de R$ {valor_deposito:.2f} realizado com sucesso.\n\nTransações diárias restantes: {LIMITE_TRANSACOES - numero_transacoes}\n\n")
        else:
            print("\nOperação falhou. Digite um valor válido.\n\n####################\n\nRetornando ao Menu Principal...\n\n")
    else:
        print("\nLimite de transações diárias atingido. Tente novamente outro dia.\n\n ")

    return saldo, extrato, numero_transacoes

def exibir_extrato(saldo, /, *, extrato):
    print("\n\n\n")
    print(" Extrato da conta ".center(30,"#"))
    print(f"\n{extrato}\n\nSaldo final: R$ {saldo:.2f}\n\n\n")
    print("#" * 30)


while True:
    opcao = input(menu)

    if opcao == 'c':
        nova_lista = cadastrar_usuario(lista_clientes)
        if nova_lista != None:
            lista_clientes = nova_lista
    elif opcao == 'cc':
        nova_lista = criar_conta(lista_contas=lista_contas, numero_conta=numero_conta, lista_clientes=lista_clientes)
        if nova_lista != None:
            lista_contas = nova_lista
            numero_conta += 1
    elif opcao == 'lu':
        listar_clientes(lista_clientes)

    elif opcao == 'lc':
        listar_contas(lista_contas, lista_clientes)

    elif opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito(apenas números ex: 100 ou 100.00):\n"))
        saldo, extrato, numero_transacoes = depositar(valor_deposito, saldo, extrato, numero_transacoes)

    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque(apenas números ex: 100 ou 100.00):\n"))
        saldo, extrato, numero_saques, numero_transacoes = sacar(valor_saque=valor_saque, saldo=saldo, extrato=extrato, numero_transacoes=numero_transacoes, numero_saques=numero_saques)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)
        
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione a operação desejada.")