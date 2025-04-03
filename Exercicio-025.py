# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite o nome de uma cidade')).strip()

print(f'É {'silva' in nome.lower()} que tem silva no nome')