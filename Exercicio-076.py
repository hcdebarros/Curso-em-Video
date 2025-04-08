# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

itens = (
    "Lápis", 1.75,
    "Caneta",  2.50,
    "Caderno", 15.90,
    "Borracha",  0.99,
    "Apontador",  1.25,
    "Mochila", 89.90,
    "Estojo", 12.00,
    "Régua" , 3.75,
    "Marcador",  4.60,
)
for i in range(0, len(itens)):
    if i % 2 == 0:
        print(f'{itens[i]:.<20}', end = '')
    else:
        print(f'R${itens[i]:>7.2f}')