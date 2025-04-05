# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

maior = 0
menor = 0
somaidade= 0
cont = 0
homemvelho = ''
for i in range(1, 5):
    nome = str(input(f'Insira o nome da {i}ª pessoa: '))
    idade = int(input(f'Insira a idade da {i}ª pessoa: '))
    sexo = str(input(f'Insira o sexo da {i}ª pessoa: (masculino ou feminino) ')).strip().lower()
    somaidade += idade

    if i == 1:
        maior == idade
        menor == idade
    if sexo == 'masculino' and idade >= maior:
        maior = idade
        homemvelho = nome
    if sexo == 'feminino' and idade < 20:
        cont += 1

if homemvelho == 0:
    homemvelho = 'Não teve homem nessa lista'
       

   

print(f'A média da idade do grupo é: {somaidade/i}')
print(f'O nome do homem mais velho é: {homemvelho}')
print(f'A quantidade de mulheres com menos de 20 anos é: {cont}')