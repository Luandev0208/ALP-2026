soma = 0
quant = int(input('Digite a quantidade de números que você quer digitar: '))
cont = quant
while cont > 0:
    cont -= 1
    num = int(input("Digite um número: "))
    soma += num
print(f"A soma é {soma}")
print(f"Foram digitados {quant} números")
print(f"A média é {soma/quant}")