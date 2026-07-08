def soma_digitos(num):
    soma = 0
    while num > 0:
        digito = num % 10
        soma += digito
        num = num // 10

    return soma

num = int(input("Digite um número: "))
resultado = soma_digitos(num)
print(resultado)