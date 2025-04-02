# Fatiamento

frase = 'Curso em Vídeo Python' # contagem começa em 0, espaços contam como caracter



print(frase[9]) # Só printa o caracter numero 9
print(frase[9:13]) # Vai do 9 até o 12 (é sempre 1 a menos do final)
print(frase[9:21:2]) # Vai pulando de 2 em 2
print(frase[:5]) # Não declara o inicio, mas declara até onde
print(frase[15:]) # Declara inicio, mas não declara até onde
print(frase[9::3]) # # Declara inicio, mas não declara até onde e pula de 3 em 3


# Análise

print(len(frase)) # Mostra o tamanho da string
print((frase.count('o'))) # Mostra quantos aparecem
print((frase.count('o',0,13))) # Mostra quantos aparecem do 0 até o 13
print((frase.find('deo'))) # Mostra onde começou esse termo
print((frase.find('Android'))) # Como não tem esse termo, retorna -1
print('Curso' in frase)


# Transformação

print(frase.replace('Python', 'Android')) # Troca onde tem Python por Android
print(frase.upper()) # Coloca tudo em maiúsculo
print(frase.lower()) # Coloca tudo em minúsculo
print(frase.capitalize()) # Coloca tudo em minúsculo, mas a primeira fica em maiúsculo
print(frase.title()) # Coloca todos as palavras com a inicial maiúsculo
print(frase.strip()) # Remove todos os espaços inúteis antes e depois dos caracteres
print(frase.rstrip()) # Remove os espaços da direita
print(frase.lstrip()) # Remove os espaços da esquerda


# Divisão

print(frase.split()) # Onde tem espaço ele vai dividir a string, gera uma lista


# Junção

print('-'.join(frase)) # Separa tudo com -
print('-'.join(frase.split())) # Junta palavras separadas com -