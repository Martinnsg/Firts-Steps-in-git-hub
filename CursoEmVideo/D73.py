#crie uma tupla com os 20 primeiros colocados do brasileirao 
tabela = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico-PR','Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo','Santos','Goias','Bragantino','Coritiba','Cuiaba','Ceará','Atlético-GO','Avaí','Juventude')
print(f'Os cinco primeiros colocados do brasileirão 2022 são: {tabela[:6]}')
print(f'Os quatro ultimos colocados do brasileirão 2022 são: {tabela[-4:]}')
p = tabela.index('Santos')
print(f'O Santos está na {p}ª posição')
print('A ordem alfabética dos clubes é: {}'.format(sorted(tabela)))