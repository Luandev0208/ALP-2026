def calculadora(v1, v2, operador):
    if operador == "+":
        resultado = v1 + v2
        return f"{v1} + {v2} = {resultado}"
    elif operador == "-":
        resultado = v1 - v2
        return f"{v1} - {v2} = {resultado}"
    elif operador == "*":
        resultado = v1 * v2
        return f"{v1} x {v2} = {resultado}"
    elif operador == "/":
        resultado = v1 / v2
        return f"{v1} / {v2} = {resultado}"
    else:
        return "Esse operador não é válido"

v1 = int(input("Digite um número: "))
op = input("Digite um operador(+, -, *, /): ")
v2 = int(input("Digite outro número: "))


resultado = calculadora(v1, v2, op)
print(resultado)