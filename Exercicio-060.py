# Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Insira um número inteiro para saber o seu fatorial: '))
print(f'Calculando {num}! = ', end = ' ')
prod = 1
cont = num
while cont > 0:
    print(f'{cont} ', end = ' ')
    if cont > 1:
        print(' x ', end = ' ')
    else:
        print('= ', end = ' ')
    prod *= cont 
    cont -= 1

print(f'{prod}')