# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = float(input('Insira o primeiro termo da PA: '))
razao = float(input('Insira a razão da PA: '))
cont = 1
termo_anterior = primeiro_termo
while cont <= 10:
    cont += 1
    print(f'{termo_anterior}', end = ' ')
    termo_anterior += razao 