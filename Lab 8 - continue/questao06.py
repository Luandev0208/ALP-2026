while True:
    valor = int(input("Digite o valor que deseja sacar: "))

    if valor < 20:
        print("Não é possível realizar esse saque.")
        continue

    if valor % 10 != 0:
        print("Não é possível realizar esse saque.")
        continue

    if valor in [30, 70]:
        print("Não é possível realizar esse saque.")
        continue

    print("Saque realizado com sucesso!")
    break