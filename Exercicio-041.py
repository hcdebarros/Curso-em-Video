#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date

ano = int(input('Digite o ano de nascimento de um atleta'))

dif = date.today().year - ano

if dif <=9:
    print('Sua categoria é MIRIM')
elif 9 < dif <= 14:
    print('Sua categoria é INFANTIL')
elif 14 < dif <= 19:
    print('Sua categoria é JÚNIOR')
elif 19 < dif <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')