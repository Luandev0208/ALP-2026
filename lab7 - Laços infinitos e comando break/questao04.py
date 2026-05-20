import random # essa deve ser a primeira linha do código
chances = 5
num_computador = random.randint(1,10)

while chances > 0:
    num_usuario = int(input('Escolha um número (1 a 10): '))
    if num_computador == num_usuario:
        print('Parabéns, você acertou o número!')
        break
    else:
        print(f'Você errou! Tente novamente.')
        chances -= 1
        if chances == 0:
            print(f'Você não acertou nenhuma vez, o número digitado pelo computador foi: {num_computador}')
