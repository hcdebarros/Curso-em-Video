# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep
cont = 0
while True:
    computador = randint(0,10)
    num = int(input('Diga um valor: '))
    escolha = int(input('Escolha uma opção:\n[ 1 ]- Ímpar\n[ 2 ]- Par'))
    soma = num + computador
    if escolha == 1:
        if soma % 2 == 0:
            print(f'Você jogou {escolha} e o computador {computador}. Total = {soma}, deu par.')
            break
        else: 
            print('Você venceu!')
            sleep(1)
            cont += 1
    elif escolha == 2:
        if soma % 2 == 0:
            print('Você venceu!')
            sleep(1)
            cont += 1
        else:
            print(f'Você jogou {escolha} e o computador {computador}. Total = {soma}, deu ímpar.')
            break
    else:
        print('Opção errada, finalizando programa.')
        break

print(f'GAME OVER! Você venceu {cont} vezes.')
    
