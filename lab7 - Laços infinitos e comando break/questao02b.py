soma = 0
contador = 0

#A variável do while está errada, pq ele está usando a variável da soma e não um contador contando o numero de vezes que o usuario digitou números, que são para digitar 10 vezes, ele estava testando até a soma dos numeros ser 10, isso estava errado
while contador < 10: 
    num = int(input("Digite um número para somar: "))
    # O while nunca ia acabar, pois não tinha nenhuma variável fazendo a subração de um contador que faça o while acabar
    contador += 1
    soma += num

