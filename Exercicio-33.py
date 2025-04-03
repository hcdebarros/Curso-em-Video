# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input('Insira o primeiro número'))
num2 = float(input('Insira o segundo número'))
num3 = float(input('Insira o terceiro número'))

ordem = [num1, num2, num3]

print(f'O maior número é: {max(ordem)}')
print(f'O menor número é: {min(ordem)}')