# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

cato = float(input('Insira o valor do cateto oposto'))
cata = float(input('Insira o valor do cateto adjacente'))
hipo = math.hypot(cato,cata)
print(f'O valor da hipotenusa é: {hipo:.2f}')