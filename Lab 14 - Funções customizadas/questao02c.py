def soma(valor1, valor2):
    s = valor1 + valor2
    return f"{valor1} + {valor2} = {s}"

valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))

resultado = soma(valor1, valor2)
print(resultado)
