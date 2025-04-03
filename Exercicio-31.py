# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

dist = float(input('Insira a distância da viagem em km'))

if dist <= 200:
    preco = dist * 0.5
    
else:
    preco = dist * 0.45
print(f'O preço da passagem será de: R${preco:.2f}')