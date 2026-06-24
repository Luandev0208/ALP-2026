valor = input("Digite um valor: ")

try:
    inteiro = int(valor)
    print("int():", inteiro)
except:
    print("int(): Erro")

try:
    decimal = float(valor)
    print("float():", decimal)
except:
    print("float(): Erro")

try:
    booleano = bool(valor)
    print("bool():", booleano)
except:
    print("bool(): Erro")
