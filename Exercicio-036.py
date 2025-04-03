# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Insira o valor da casa: '))
salario = float(input('Insira o salário: '))
anos = int(input('Insira em quantos anos será o financiamento: '))

mensalidade = valor / (anos * 12)

if mensalidade > salario * 0.3:
    print('O financiamento foi negado')
else:
    print(f'A mensalidade do empréstimo ficou em: R${mensalidade:.2f}')