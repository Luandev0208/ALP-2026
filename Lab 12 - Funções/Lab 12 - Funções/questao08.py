import datetime

nome1 = input("Nome da primeira pessoa: ")
data1_str = input("Data de nascimento (dd/mm/aaaa): ")

nome2 = input("Nome da segunda pessoa: ")
data2_str = input("Data de nascimento (dd/mm/aaaa): ")

data1 = datetime.datetime.strptime(data1_str, "%d/%m/%Y")
data2 = datetime.datetime.strptime(data2_str, "%d/%m/%Y")

hoje = datetime.datetime.now()

aniv1 = datetime.datetime(hoje.year, data1.month, data1.day)
aniv2 = datetime.datetime(hoje.year, data2.month, data2.day)

if aniv1 < hoje:
    aniv1 = datetime.datetime(hoje.year + 1, data1.month, data1.day)

if aniv2 < hoje:
    aniv2 = datetime.datetime(hoje.year + 1, data2.month, data2.day)

dias1 = (aniv1 - hoje).days
dias2 = (aniv2 - hoje).days

if dias1 < dias2:
    print(f"O aniversário mais próximo é o de {nome1}.")
else:
    print(f"O aniversário mais próximo é o de {nome2}.")
