# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Insira o valor da largura da parede'))
altura = float(input('Insira o valor da altura da parede'))
area = largura * altura
print(f'A área da parede é de: {area}m² \nSerão necessários {area/2} litros de tinta')