# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep as sl

escolha = int(input('Escolha entre:\n[ 0 ]- Pedra\n[ 1 ]- Papel\n[ 2 ]- Tesoura\nO que você irá escolher? '))
print('Pedra')
sl(0.5)
print('Papel')
sl(0.5)
print('e Tesouuuuuuu')
sl(1)
print('Ra')
sl(0.5)
computador = randint(0,2)

if (escolha == 0 and computador == 0) or (escolha == 1 and computador == 1) or (escolha == 2 and computador ==2):
    print('Foi empate.')
elif (escolha == 0 and computador == 2) or (escolha == 1 and computador == 0) or (escolha == 2 and computador == 1):
    print('Parabéns, você venceu!')
elif (escolha == 0 and computador == 1) or (escolha == 1 and computador == 2) or (escolha == 3 and computador == 0):
    print('Infelizmente você perdeu! ')


# from random import randint
# itens = ('Pedra', 'Papel', 'Tesoura')
# computador = randint(0,2)