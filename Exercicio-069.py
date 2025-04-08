# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

conthomens = contmulheres = contidade = 0
while True:
    idade = int(input('Insira a idade do paciente: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Insira o sexo do paciente (F- feminino, M- Masculino) ')).strip().upper()[0]

    if idade > 18:
        contidade += 1
    if sexo == 'M':
        conthomens += 1
    if sexo == 'F':
        if idade < 20:
            contmulheres += 1
    
    continuar = str(input('Você deseja cadastrar mais algum paciente? (S- Sim, N- Não) ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Foram cadastradas {contidade} pessoa(s) com mais de 18 anos.')
print(f'Foram cadastrados {conthomens} homem(ns).')
print(f'Foram cadastradas {contmulheres} mulher(es) com menos de 20 anos.')