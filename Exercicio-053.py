# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input('Insira uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

# inverso = junto[::-1] (isso retira o for)
for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]

if inverso == junto:
    print('A frase é um palíndromo')
else: 
    print('Não é palíndromo')
