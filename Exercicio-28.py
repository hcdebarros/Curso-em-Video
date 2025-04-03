# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

num = random.randint(0,5)
numus = int(input('Digite um numero de 0 a 5'))

if numus == num:
    print('Parabéns você acertou!')
else:
    print(f'Infelizmente você errou. O número certo era {num}')