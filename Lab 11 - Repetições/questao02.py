while True:
    resp = input("Você quer saber como manter uma pessoa ingênua ocupada por horas? S/N: ")
    if resp in ["s", "S", "sim", "SIM"]:
        continue
    elif resp in ["n", "N", "não", "NÃO"]:
        print("Obrigada. Tenha um bom dia!")
        break
    else:
        print(f'"{resp}" não é uma resposta válida de sim/não.')



#resp == 'S' or resp == 'SIM' or resp == 'SI' or resp == 'SM'