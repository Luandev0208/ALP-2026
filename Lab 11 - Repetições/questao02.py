while True:
    resp = input("Você quer saber como manter uma pessoa ingênua ocupada por horas? S/N: ")
    if resp == 's' or resp == 'S' or resp == 'sim' or resp == "SIM":
        continue
    elif resp == 'n' or resp == 'N' or resp == 'não' or resp == 'NÃO'or resp == 'nao' or resp == 'NAO':
        print("Obrigado. Tenha um bom dia!")
        break
    else:
        print(f'"{resp}" não é uma resposta válida de sim/não.')



