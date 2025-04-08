# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Você quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    for i in range(0,11):
        prod = num * i
        print(f'{num} x {i} = {prod}')
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')