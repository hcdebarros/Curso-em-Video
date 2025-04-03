# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


dist = float(input('Insira quantos quilômetros foram percorridos'))
dias = int(input('Insira a quantidade de dias alugado'))

print(f'O valor total do aluguel é: R${(dias*60 + dist*0.15):.2f}')