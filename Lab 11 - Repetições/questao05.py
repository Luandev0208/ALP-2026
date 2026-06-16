import random

secreto = str(random.randint(100, 999))

for chance in range(1, 11):
    print(f"==== Chance {chance} ====")

    palpite = input("Palpite: ")

    resultado = ""

    for i in range(3):
        if palpite[i] == secreto[i]:
            resultado += "+"
        elif palpite[i] in secreto:
            resultado += "!"
        else:
            resultado += "_"

    print("Saída:", resultado)

    if resultado == "+++":
        print("Parabéns! Você acertou!")
        break

else:
    print("Suas 10 chances acabaram!")
    print("O número secreto era:", secreto)