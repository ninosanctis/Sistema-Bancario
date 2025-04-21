import textwrap


def menu():
    menu = """ \n
 Escolha uma opção:

  [1] - Depositar
  [2] - Sacar
  [3] - Extrato
  [4] - Criar conta
  [5] - Listar contas
  [6] - Novo Usuario
  [0] - Sair

=>"""

    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=======Valor depositado com sucesso!=======\n")
        print(f"Saldo atual: R$ {saldo:.2f}\n")
        print("===========================================")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\nValor inválido para saque. Saldo insuficiente.")
    elif excedeu_limite:
        print("\nValor inválido para saque. Valor acima do limite.")
    elif excedeu_saques:
        print("\nNúmero máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=======Valor de saque realizado com sucesso!=======\n")
        print(f"Saldo atual: R$ {saldo:.2f}\n")
        print("===========================================")
    else:
        print("\nValor inválido para saque.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n======= Extrato =======")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("======= Fim do extrato =======")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n======= Usuário já cadastrado! =======\n")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro): ")

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    print("\n======= Usuário cadastrado com sucesso! =======\n")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n======= Conta criada com sucesso! =======\n")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    print("\n======= Usuário não encontrado! =======\n")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: {conta['agencia']},
        Conta: {conta['numero_conta']},
        Titular: {conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 5
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor a ser depositado: R$"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor a ser sacado: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                print("\nConta criada com sucesso!")
            else:
                print("\nOperação falhou! O usuário selecionado ainda nao possui conta.")

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        else:
            print("\n======= Sistema encerrado! =======\n")
            break


main()
