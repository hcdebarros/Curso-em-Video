# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


lista = []

while True:
    nome = str(input('Insira o nome do aluno: ')).strip()
    nota1 = float(input('Insira a primeira nota do aluno: '))
    nota2 = float(input('Insira a segunda nota do aluno: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    escolha = input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ').strip().upper()[0]

    while escolha not in 'SN':
        print('Opção inválida, tente novamente.')
        escolha = input('Deseja inserir outro valor?\n[ S ]- Sim\n[ N ]- Não ').strip().upper()[0]

    if escolha == 'N':
        break

print(f'{'No.':<4}{'NOME':<10}{'MEDIA':>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')