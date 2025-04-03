# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a segunda nota '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'Aluno foi reprovado, pois obteve {media} de média')
elif 5 < media < 7:
    print(f'Aluno está na recuperação, pois obteve {media} de média')
else:
    print(f'Aluno foi aprovado com média {media}')