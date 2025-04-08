# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
for i in range(0,5):
    num = int(input('Insira um valor: '))
    numeros.append(num)
print(f'O maior número digitado foi {max(numeros)} nas posições', end = ' ')
for a, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{a}', end = ' ')
print(f'\nO maenor número digitado foi {min(numeros)} nas posições', end = ' ')
for b, c in enumerate(numeros):
    if c == min(numeros):
        print(f'{b}', end = ' ')
