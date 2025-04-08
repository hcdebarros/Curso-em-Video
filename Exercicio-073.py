# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Sport.


times= ("Internacional", "Corinthians", "Ceará", "Fortaleza", "Botafogo",
    "Flamengo", "Palmeiras", "Fluminense", "Grêmio", "Vasco",
    "Cruzeiro", "Atlético-MG", "São Paulo", "Athletico Paranaense", "Cuiabá",
    "Criciúma", "Atlético Goianiense", "Bahia", "Sport", "Vitória"
)

print(f'Os cinco primeiros times são: {times[:5]}')
print(f'Os últimos 4 colocados são: {times[16:]}')
print(f'Os times em ordem alfabética fica: {sorted(times)}')
print(f'O sport está na {times.index('Sport') + 1}ª posição')
