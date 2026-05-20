conta = 0
print('''Cardápio
1. Açaí 300ml - R$ 12
2. Mousse - R$ 6,50
3. Salada de frutas - R$ 10
4. Fechar a conta
''')

while True:
    opcao = input('Digite a opção que você deseja: ')
    if opcao == '1':
        conta += 12
    elif opcao == '2':
        conta += 6.5
    elif opcao == '3':
        conta += 10
    elif opcao == '4': break
    else: 
        print('Essa opção é inválida, tente novamente.')
        
print(f'O valor da sua conta final é de R${conta}')
