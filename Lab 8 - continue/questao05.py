total = 0

while True:
    print("\n=== CARDÁPIO ===")
    print("1 - Açaí 300ml - R$12")
    print("2 - Mousse - R$6,50")
    print("3 - Salada de frutas - R$10")
    print("4 - Fechar conta")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        total += 12
    elif opcao == 2:
        total += 6.50
    elif opcao == 3:
        total += 10
    elif opcao == 4:
        print(f"Total da conta: R${total:.2f}")
        break
    else:
        print("Opção inválida!")
        continue
