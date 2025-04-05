# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

prim = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))

for i in range(prim, razao*10, razao):
    print(i, end =' ')