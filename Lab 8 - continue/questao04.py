soma = 0

while True:
    num = int(input("Digite um número: "))

    if num == 0:
        break

    if num < 0:
        continue

    soma += num

    if soma > 100:
        break

print(f"Soma total: {soma}")
