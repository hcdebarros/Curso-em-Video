# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

linha1 = []
linha2 = []
linha3 = []
cont = 0
for i in range(0,3):
    num = int(input(f'Digite um valor para [{cont},{i}] '))
    linha1.append(num)
cont +=1
for i in range(0,3):
    num = int(input(f'Digite um valor para [{cont},{i}] '))
    linha2.append(num)
cont +=1
for i in range(0,3):
    num = int(input(f'Digite um valor para [{cont},{i}] '))
    linha3.append(num)
print(f"""{linha1}
{linha2}
{linha3}
""")