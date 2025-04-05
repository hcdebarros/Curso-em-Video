# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

from time import sleep

sexo = ' '

while sexo not in 'MmFf':
    sexo = str(input('Digite o sexo:\n[ M ]- Masculino\n[ F ]- Feminino ')).strip().upper()[0]
    
    if sexo not in 'MmFf':
        print('Opção inválida.')
        sleep(1)
if sexo == 'M':
    print('O sexo é masculino')
else:
    print('O sexo é feminino')
        