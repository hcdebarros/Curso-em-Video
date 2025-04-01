# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n1 = int(input('Digite um número inteiro'))

for i in range(11):
    print(f'{n1} X {i:2} = {n1*i}')