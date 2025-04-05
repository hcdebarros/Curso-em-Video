# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tab = int(input('Você deseja a tabuada de qual número?'))
for i in range(11):
    prod = tab * i
    print(f'{tab} x {i} = {prod}')