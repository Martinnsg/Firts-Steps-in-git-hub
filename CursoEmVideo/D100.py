from random import randint
def par(lista):
    soma = 0
    print(f'Sorteando 5 valores na lista: ',end='')
    for i in range (0,5):
        n = randint(1,100)
        lista.append(n)
        print(n,end=' ')
        if n%2 == 0:
            soma += n
    return soma

n = list()
s = par(n)
print(f'\nA soma dos valores da lista é: {s}')