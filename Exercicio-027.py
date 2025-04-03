# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo').strip()
separado = nome.split()
print(f'O primeiro nome é {separado[0]} e o último nome é {separado[len(separado) - 1]}')