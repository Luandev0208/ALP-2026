num_itens = 0 
itens = ''

while num_itens < 5:
    item = input('Digite todos os itens do personagem (1 por vez) ou sair caso acabem os itens: ').lower().strip()
    if item == 'sair':
        break
    num_itens += 1
    itens += item
    itens += ', '
print(itens)
