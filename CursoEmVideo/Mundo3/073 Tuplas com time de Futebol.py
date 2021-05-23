"""
exercise: 073
objective:  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

times = ('América-MG', 'Athletico-PR', 'Atlético Goianience', 'Bahia', 'Ceará', 'Chapecoense',
         'Corinthians', 'Cuìabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional',
         'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'Sport Recife', 'São Paulo')
print('-='*30)
print(f'Lista de time do Brasileirão: {times}')
print('-='*30)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*30)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética {sorted(times)}')
print('-='*30)
print(f'O Chapecoense está ma {times.index("Chapecoense") + 1}º posição.')
