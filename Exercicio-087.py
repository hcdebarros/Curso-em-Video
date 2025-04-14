# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

linha1 = []
linha2 = []
linha3 = []
cont = soma = 0
for i in range(0,3):
    num = int(input(f'Digite um valor para [{cont},{i}] '))
    linha1.append(num)
    if num % 2 == 0:
        soma += num
cont +=1
for i in range(0,3):
    num = int(input(f'Digite um valor para [{cont},{i}] '))
    linha2.append(num)
    if num % 2 == 0:
        soma += num
cont +=1
for i in range(0,3):
    num = int(input(f'Digite um valor para [{cont},{i}] '))
    linha3.append(num)
    if num % 2 == 0:
        soma += num
print(f"""{linha1}
{linha2}
{linha3}
""")
print(f'A soma de todos os valores pares digitados é {soma}')
print(f'a soma dos valores da terceira coluna é {sum(linha3)}')
print(f'O maior valor da segunda linha é {max(linha2)}')