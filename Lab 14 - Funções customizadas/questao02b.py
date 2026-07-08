def ola(nome, genero):
    if genero == "N" or genero == "n":
        return f"Olá {nome}, boas vindas!"
    elif genero == "F" or genero == "f":
        print f"Olá {nome}, bem vinda!"
    elif genero == "M" or genero == "m":
        return f"Olá {nome}, bem vindo!"
    else:
        return "Você não digitou nenhuma opção válida!"

nome = input("Digite seu nome: ")
print("Escolha uma das opções de gênero (feminino(F), masculino(M) ou neutro(N)): ")
genero = input("Digite seu gênero: ")

resultado = ola(nome, genero)
print(resultado)
