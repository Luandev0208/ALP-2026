soma = 0
produto = 3
valor = int(input("Digite um valor: "))
cont = 1
while (cont <= valor):
    if soma > produto:
        break
    soma += cont
    if cont % 2 != 0:
        produto *= cont
    cont += 1
print(soma, produto)