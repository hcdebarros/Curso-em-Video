# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

from time import sleep

lista = []

while True:
    num = int(input('Insira um valor: '))
    if num in lista:
        print('Número já está na lista. Digite outro número')

    else:
        lista.append(num)
        escolha = str(input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ')).strip().upper()[0]

        while escolha not in 'SN':
            print('Opção inválida, tente novamente.')
            sleep(0.8)
            escolha = str(input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ')).strip().upper()[0]
        if escolha == 'N':
            break
lista.sort()
print(f'{lista}')
