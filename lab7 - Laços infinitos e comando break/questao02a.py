N = int(input("Quantos números quer digitar?"))
contador = 1
impares = 0

while contador <= N:
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1
    #Não tem nada para fazer o número do contador aumentar e com isso o while terminar em algum momento
    contador += 1

print(f"Quantidade de ímpares: {impares}")
