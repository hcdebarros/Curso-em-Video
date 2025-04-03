# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

num1 = int(input('Insira o primeiro número'))
num2 = int(input('Insira o segundo número'))

if num1 > num2:
    print('O primeiro número é maior')
elif num2 > num1:
    print('O segundo número é maior')
else:
    print(f'Os dois são iguais')