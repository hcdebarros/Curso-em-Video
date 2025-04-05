# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0

for i in range(7):
    ano = int(input('Insira o ano de nascimento: '))

    if date.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoa(s) atingiram a maioridade')
print(f'{menor} pessoas(s) não atingiram a maioridade')