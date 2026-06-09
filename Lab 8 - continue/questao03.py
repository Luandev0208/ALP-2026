import random

secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input("Adivinhe o número (1 a 10): "))

    if palpite < 1 or palpite > 10:
        print("Número inválido!")
        continue

    if palpite == secreto:
        print("Parabéns! Você acertou!")
        break

    chances -= 1
    print(f"Errou! Restam {chances} chances.")

if chances == 0:
    print(f"Você perdeu! O número era {secreto}.")
