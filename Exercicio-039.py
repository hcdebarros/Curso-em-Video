# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = date.today().year
nasc = int(input('Insira o ano de nascimento do jovem'))
dif = ano - nasc
if dif > 18:
    print(f'Já passou do tempo de se alistar em {dif-18} anos')
elif dif < 18:
    print(f'Ainda vai se alistar e faltam {18-dif} anos')
else:
    print('Está na data exata para se alistar')