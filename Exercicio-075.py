# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))
numeros = (num1, num2, num3, num4)
cont = numeros.count(9)

if cont == 0:
    print(f'O número 9 não apareceu nenhuma vez')
else:
    print(f'O número 9 apareceu {cont} vez(es)')

if 3 in numeros:
    print(f'O primeiro "3" foi encontrado na posição {numeros.index(3) + 1}')
else:
    print('O número "3" não apareceu.')


print('Os números pares são: ', end = '')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end = ' ')

