while True:
    valor = int(input("Digite o valor que deseja sacar: "))

    if valor < 20:
        print("Não é possível realizar esse saque.")
        continue

    possivel = False
    nota100 = 0

    while nota100 * 100 <= valor:
        nota50 = 0

        while nota100 * 100 + nota50 * 50 <= valor:
            restante = valor - (nota100 * 100 + nota50 * 50)

            if restante % 20 == 0:
                possivel = True
                break

            nota50 += 1

        if possivel:
            break

        nota100 += 1

    if possivel:
        print("Saque realizado com sucesso!")
        break
    else:
        print("Não é possível realizar esse saque.")