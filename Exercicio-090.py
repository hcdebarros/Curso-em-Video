dicio = {}
dicio['nome'] = input('Insira o nome do aluno: ')
dicio['media'] = float(input('Insira a média do aluno: '))

if dicio['media'] < 7:
    dicio['situacao'] = 'Recuperação'
else:
    dicio['situacao'] = 'Aprovado'

print(f'O nome é {dicio['nome']}')
print(f'A média é {dicio['media']}')
print(f'A situação é {dicio['situacao']}')


