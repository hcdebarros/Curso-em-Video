# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = float(input('Insira o primeiro termo da PA: '))
razao = float(input('Insira a razão da PA: '))
cont = 10
termo_anterior = primeiro_termo
soma_termos = 0

while True:
    while soma_termos < cont:
        print(f'{termo_anterior}', end = ' ')
        termo_anterior += razao 
        soma_termos += 1

    termos = int(input('\nQuantos termos você quer mostrar a mais? '))
   
    if termos == 0:
        print(f'Progressão finalizada com {soma_termos} termos mostrados')
        break
    cont += termos
