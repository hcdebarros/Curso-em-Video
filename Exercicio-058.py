# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

num = randint(0,10)

escolha = int(input('Escolha um numero entre 0 e 10: '))
cont = 1
while escolha != num:
    print('Você errou, mas darei outra chance.')
    escolha = int(input('Escolha um numero entre 0 e 10: ')) 
    cont += 1
print(f'Você acertou na {cont}ª tentativa, Parabéns!')