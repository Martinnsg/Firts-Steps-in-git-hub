# variavel simples = só cabe um
# variavel composta = cabe mais de uma
#     - tuplas
#     - listas
#     - dicionarios
# AS TUPLAS SAO IMUTAVEIS
# print(c.index(4)) mostra em que posição estao o numero 4 na tupla c, pega a primeira ocorrencia
# print(c.count(5)) mostra quantas vezes aparce 5 na tupla c

lanche = ('hamburguer','suco','pizza','pudim','batata frita')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')