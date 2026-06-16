import random
import time

pontos1 = 0
pontos2 = 0

while pontos1 < 50 and pontos2 < 50:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    jogador1 = int(input(f"Jogador 1 ({pontos1} pontos): Qual o seu palpite para a soma dos dados? "))
    jogador2 = int(input(f"Jogador 2 ({pontos2} pontos): Qual o seu palpite para a soma dos dados? "))

    print("🎲 Rolando os dados...")
    time.sleep(1)
    print(f'Dado 1: {dado1}')
    time.sleep(1)
    print(f'Dado 2: {dado2}')

    soma = dado1 + dado2
    dif1 = abs(jogador1 - soma)
    dif2 = abs(jogador2 - soma)

    if dif1 < dif2:
        pontos1 += 5
        print(f"Resultado: 🏆 -> Jogador 1 chegou mais perto e ganhou 5 pontos.")
    elif dif1 > dif2:
        pontos2 += 5
        print(f"Resultado: 🏆 -> Jogador 2 chegou mais perto e ganhou 5 pontos.")
    else:
        pontos1 += 2
        pontos2 += 2
        print(f"Resultado: ⚖️ EMPATE! Cada um ganha 2 pontos!")

if pontos1 >= 50:
    print("O Campeão foi...")
    time.sleep(1)
    print("Jogador 1")

elif pontos2 >= 50:
    print("O Campeão foi...")
    time.sleep(1)
    print("Jogador 2")