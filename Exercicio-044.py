# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

conta = float(input('Insira o valor a ser pago. '))
pagamento = int(input('Insira a forma de pagamento: \n[ 1 ] - à vista dinheiro/cheque\n[ 2 ]- à vista no cartão \n[ 3 ]- em até 2x no cartão\n[ 4 ]- 3x ou mais no cartão '))

if pagamento == 1:
    preco = conta * 0.9
    print(f'O valor a ser pago será de: R${preco:.2f}')
elif pagamento == 2:
    preco = conta * 0.95
    print(f'O valor a ser pago será de: R${preco:.2f}')
elif pagamento == 3:
    preco = conta
    print(f'O valor a ser pago será de: R${preco:.2f} e o valor de cada parcela será de: R${preco/2:.2f}')
elif pagamento == 4:
    preco = conta * 1.2
    parc = int(input('Será em quantas parcelas? '))
    print(f'O valor a ser pago será de: R${preco:.2f} e o valor de cada parcela será de: R${preco/parc:.2f}')
else:
    print('Opção invlálida')