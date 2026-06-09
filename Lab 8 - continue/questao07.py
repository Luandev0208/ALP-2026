degrau = 1

while True:
    print(f"\nDegrau atual: {degrau}")

    passos = int(input("Digite o número de passos (1-6) ou 0 para sair: "))

    if passos == 0:
        print("Jogo encerrado.")
        break

    if passos < 1 or passos > 6:
        print("Valor inválido, tente novamente!")
        continue

    degrau += passos

    if degrau % 3 == 0:
        print(f"[Degrau: {degrau} -> Múltiplo de 3] Volte 1 degrau!")
        degrau -= 1
    elif degrau % 5 == 0:
        print(f"[Degrau: {degrau} -> Múltiplo de 5] Avance 1 degrau!")
        degrau += 1
    elif degrau % 7 == 0:
        print(f"[Degrau: {degrau} -> Múltiplo de 7] Avance 4 degraus!")
        degrau += 4
    elif degrau % 11 == 0:
        print(f"[Degrau: {degrau} -> Múltiplo de 11] Volte para o início!")
        degrau = 1

    if degrau >= 100:
        print("Parabéns! Você chegou ao degrau 100!")
        break
