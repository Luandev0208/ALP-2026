vitorias = 0
empates = 0
derrotas = 0
pontos = 0

jogos = int(input("Quantidade de jogos: "))

for i in range(jogos):
    gols_galo = int(input("Gols do Galo: "))
    gols_adversario = int(input("Gols do adversário: "))

    if gols_galo > gols_adversario:
        vitorias += 1
        pontos += 3
    elif gols_galo == gols_adversario:
        empates += 1
        pontos += 1
    else:
        derrotas += 1

print(f"O galo venceu {vitorias} partidas")
print(f"O galo empatou {empates} partidas")
print(f"O galo perdeu {derrotas} partidas")
print(f"O galo fez {pontos} pontos")
