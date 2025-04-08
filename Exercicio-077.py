# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = (
    "abacaxi",
    "relampago",
    "cafune",
    "girassol",
    "pirulito",
    "montanha",
    "vagalume",
    "maracuja",
    "tapioca",
    "espaguete",
    "jacare",
    "xilofone"
)

for i in palavras:
        print(f'\nNa palavra {i} temos ', end = '')
        for letra in i:
            if letra.lower() in 'aeiou':
                print(letra, end = ' ')
        