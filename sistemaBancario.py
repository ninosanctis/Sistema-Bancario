menu = """
 Escolha uma opção:

  [1] - Depositar
  [2] - Sacar
  [3] - Extrato
  [0] - Sair

=>"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Valor depositado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "2":
        valor = float(input("Informe o valor a ser sacado: "))

        if numero_saques < LIMITE_SAQUES:
            if valor <= saldo and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!")
                print(f"Saldo atual: R$ {saldo:.2f}")
            else:
                print(
                    "Valor inválido para saque. Saldo insuficiente ou valor acima do limite.")
        else:
            print("Número máximo de saques atingido.")

    elif opcao == "3":
        print("====== Extrato ======")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
        print("====== Fim do extrato ======")
    elif opcao == "0":
        print("Saindo...")
        print("Obrigado por usar o sistema!")
        break
    else:
        print("Opção inválida. Tente novamente.")
        print("========================")
