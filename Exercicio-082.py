# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.


lista = []
pares = []
impares = []
while True:
    num = int(input('Insira um número: '))
    lista.append(num)
    escolha = str(input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Opção inválida, tente novamente.')
        escolha = str(input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ')).strip().upper()[0]
    if escolha == 'N':
        break
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(lista)
print(pares)
print(impares)