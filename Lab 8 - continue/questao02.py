cont = 5

while cont > 0:
    num = int(input("Digite um número inteiro: "))
    cont -= 1

    if num % 2 == 0:
        continue  # Se for par, pula o print e volta para o início do loop

    print(f"{num} é um número ímpar")
