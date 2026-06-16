import random
import time

while True:
    prob = random.randint(1,10)
    resp = input('Você deseja fazer uma pergunta? S/N: ')

    if resp in ["n", "N", "não", "NÃO", "nao", "NAO"]:
        break

    pergunta = input("Digite a sua pergunta: ")

    if prob <= 5: resposta = 'SIM'
    else: resposta = 'NÃO'

    time.sleep(2)
    print('Deixe-me pensar.........')
    time.sleep(2)
    print('Estou quase.............')
    time.sleep(2)
    print('Eu tenho uma resposta!')
    time.sleep(2)
    print(resposta)