import random
def roleta():
    numero = random.randint(1,36)
    if numero % 2 == 0:
        return f"{numero}, Preto"
    else:
        return f"{numero}, Vermelho" 

resultado = roleta()
print(resultado)
