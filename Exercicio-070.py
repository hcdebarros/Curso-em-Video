# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

from time import sleep

soma = cont = produto = precomenor = 0
nomemenor = ' '

while True:
    nome = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: '))
    mais = str(input('Irá adicionar mais algum produto?\n[ S ]- Sim\n[ N ]- Não ')).strip().upper()[0]
    soma += preco
    produto += 1
        
    if preco > 1000:
        cont += 1
    if produto == 1:
        precomenor = preco
        nomemenor = nome
    else:
        if preco < precomenor:
            precomenor = preco
            nomemenor = nome

    while mais not in 'SN':
        print('Opção inválida, tente novamente.')
        sleep(1)
        mais = str(input('Irá adicionar mais algum produto?\n[ S ]- Sim\n[ N ]- Não ')).strip().upper()[0]
    if mais == 'N':
        break

print(f'Total da compra foi de: R${soma:.2f}')
print(f'{cont} produtos custam mais do que R$1000,00')
print(f'O produto mais barato é: {nomemenor}')

