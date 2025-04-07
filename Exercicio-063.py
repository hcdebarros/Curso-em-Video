# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

qtd = int(input('Insira a quantidade de termos que quer mostrar: '))
cont = 3
primeiro = 0
segundo = 1
cont = 3

if qtd == 0:
    print('Não tem termos para serem mostrados.')
elif qtd == 1:
    print(f'{primeiro}', end = ' ')
else:
    print(f'{primeiro} {segundo}', end = ' ')

        
while cont <= qtd:
    termo = primeiro + segundo
    print(termo, end = ' ')
    cont += 1
    primeiro = segundo
    segundo = termo



