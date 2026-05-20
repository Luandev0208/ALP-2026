chances = 5
palavra_secreta = 'batata'
while chances > 0: 
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances")
    chances -= 1
    if palavra == 'batata': #Se o usuário acertar a palavra, ele vai mandar a mensagem que está no print dentro do if e terminar a execução do while
        print("Você acertou a palavra, toma aqui uma batata 🥔")
        break
    # O usuário terá 5 chances para acertar a palavra, se ele errar em todas as tentativas, o while irá terminar e não irá executar o if, ou seja, ele não vai ganhar/acertar