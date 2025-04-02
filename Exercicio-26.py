# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase')).strip().lower()
print(f'A frase contém {frase.count('a')} letras a.')
print(f'A primeira aparição de um a é na posição: {frase.lower().find('a') + 1} \nA ultima aparição é na posição {frase.rfind('a') + 1}')