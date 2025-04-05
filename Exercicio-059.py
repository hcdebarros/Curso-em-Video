# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

num1 = int(input('Insira o primeiro valor: '))
num2 = int(input('Insira o segundo valor: '))

print('O que você deseja?')
sleep(1)
while True:
    cont = int(input("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa """))

    if cont > 5 and cont <= 0:
        print('Opção inválida, tente novamente. ')
        sleep(1)
    if cont == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} = {soma}')
        sleep(1)
    elif cont == 2:
        prod = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} = {prod}')
        sleep(1)
    elif cont == 3:
        if num1 > num2:
            maior = num1
            print(f'O maior número é: {maior}')
            sleep(1)
        else:
            maior = num2
            print(f'O maior número é: {maior}')
            sleep(1)
    elif cont == 4:
        print('O que você deseja?')
        num1 = int(input('Insira o primeiro valor: '))
        num2 = int(input('Insira o segundo valor: '))
        sleep(1)
    elif cont == 5:
        print('Você saiu.')
        break

