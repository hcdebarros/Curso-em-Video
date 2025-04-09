# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:  
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.                                                                                                   
# C) Uma listagem com as pessoas mais leves.

# dados = []
# lista = []
# pesado = []
# leve = []
# maior = menor = contl = contp = 0
# while True:
#     dados.append(input('Insira o nome da pessoa: '))
#     dados.append(float(input('Insira o peso da pessoa: ')))
#     lista.append(dados[:])
#     dados.clear()
#     escolha = str(input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ')).strip().upper()[0]
#     while escolha not in 'SN':
#         print('Opção inválida, tente novamente.')
#         escolha = str(input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ')).strip().upper()[0]
#     if escolha == 'N':
#         break
# for i, pessoa in enumerate(lista):
#     nome, peso = pessoa
#     if i == 0:
#         maior = menor = peso
        
#     if i[1] >= maior:
#         maior = i[1]
#         pesado.append(i[0])
#     if i[1] > (i-1)[1]:
#         pesado.pop()
#         pesado.append(i[1]) 
#     else:
#         print('teste')
# print(pesado)
# print(f'Foram cadastradas {len(lista)} pessoas.')




dados = []
lista = []
pesado = []
leve = []
maior = menor = 0

while True:
    dados.append(input('Insira o nome da pessoa: '))
    dados.append(float(input('Insira o peso da pessoa: ')))
    lista.append(dados[:])
    dados.clear()

    escolha = input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ').strip().upper()[0]
    while escolha not in 'SN':
        print('Opção inválida, tente novamente.')
        escolha = input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ').strip().upper()[0]
    if escolha == 'N':
        break

for i, pessoa in enumerate(lista):
    nome, peso = pessoa
    if i == 0:
        maior = menor = peso
        pesado = [nome]
        leve = [nome]
    else:
        if peso > maior:
            maior = peso
            pesado = [nome]
        elif peso == maior:
            pesado.append(nome)

        if peso < menor:
            menor = peso
            leve = [nome]
        elif peso == menor:
            leve.append(nome)

print(f'Foram cadastradas {len(lista)} pessoas.')

print(f'O maior peso foi {maior}kg. Total de {len(pesado)} pessoa(s) com esse peso:')
print(' -> ' + ', '.join(pesado))

print(f'O menor peso foi {menor}kg. Total de {len(leve)} pessoa(s) com esse peso:')
print(' -> ' + ', '.join(leve))
