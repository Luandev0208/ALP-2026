import time
def contagem_regressiva(num):
    while num >= 0:
        print(num)
        time.sleep(1)
        num -= 1

num = int(input("Digite um número: "))
contagem_regressiva(num)
