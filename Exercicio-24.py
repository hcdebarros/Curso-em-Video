# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome = str(input('Digite o nome de uma cidade')).strip()
separado = nome.lower().split()
print(f'É {'santo' in separado[0]} que tem santo no começo do nome da cidade')