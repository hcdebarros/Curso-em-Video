# Crie um programa que vai ler vários números e colocar em uma lista.                 
# Depois disso, mostre:                                           
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.                                                                                         
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    num = int(input('Insira um número: '))
    lista.append(num)
    escolha = str(input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Opção inválida, tente novamente.')
        escolha = str(input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ')).strip().upper()[0]
    if escolha == 'N':
        break
lista.sort(reverse = True)
print(lista)
print(f'Foram digitados {len(lista)} números.')
print(f'Os números em ordem decrescente são {lista}')
if 5 not in lista:
    print('O número 5 não foi digitado.')
else:
    print('O número 5 está na lista.')