# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# from random import randint
# lista = []
# lista1 = []
# escolha = int(input('Quantos jogos você quer? '))

# for i in range(0,escolha):
#     for i in range(6):
#         computador = randint(1,60)
#         lista1.append(computador)
#     print(lista1)
#     lista.append([computador])
# print(lista)
# print(lista1)


from random import randint

lista = []
escolha = int(input('Quantos jogos você quer? '))

for i in range(escolha):
    lista1 = []  
    while len(lista1) < 6:
        computador = randint(1, 60)
        if computador not in lista1:  
            lista1.append(computador)
    lista.append(lista1)  # adiciona a lista do jogo completo
    print(f"Jogo {i+1}: {sorted(lista1)}")  # printa o jogo na ordem crescente (estilo loteria)

print('\nTodos os jogos:', lista)
