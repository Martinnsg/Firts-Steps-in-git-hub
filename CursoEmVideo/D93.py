#cadastro de jogador de futebol
total = 0
jogador = dict()
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
n = int(input(f'Quantas partidas jogadas pelo {jogador["nome"]}: '))
for i in range (0,n):
    partidas.append(int(input(f'Quantos gols ele fez na partida {i+1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
