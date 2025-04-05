# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pessoas = []

for i in range(1, 6):
    peso = float(input(f'Insira o peso da {i}ª pessoa'))

    pessoas.append(peso)
print(f'O maior peso foi: {max(pessoas)}')
print(f'O menor peso foi: {min(pessoas)}')