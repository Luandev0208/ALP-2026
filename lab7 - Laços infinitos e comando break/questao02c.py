#O maior tem que ser definido com -inf, pq assim sempre o maior vai ser maior que o número que o usuário digitar e o objetivo dele é testar o menor número que usuário digitar 
maior = float('-inf')
#A variável da soma não tinha sido criada
soma = 0
while soma <= 10: 
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num
print('O maior número é', maior)

