# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = int(input('Insira um número inteiro: '))
cont = 1
soma = maior = menor = num
num1 = soma =  0

while True:
    continuar = int(input('Você deseja continuar a digitar valores? \n[ 1 ] - Sim\n[ 2 ] - Não'))
    soma += num1
    
    if continuar == 1:
        num1 = int(input('Insira um número inteiro: '))
        if num1 > maior:
            maior = num1
        elif num1 < menor:
            menor = num1
        cont += 1
                   
    elif continuar == 2:
        print('Você saiu do programa')
        break
    else:
        print('Opção inválida, tente novamente.')
print(soma)
print(f'{soma/cont:.2f}')
print(maior)
print(menor)
        

