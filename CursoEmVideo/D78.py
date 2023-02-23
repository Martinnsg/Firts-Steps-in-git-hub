#faça um programa que leia 5 valores numericos e guarde em um lista
#no final mostre o maior e o menor valor e suas respectivas posições
lista = lp = list()
mai = 0
men = 0
for c in range (0,5):
    lista.append(int(input('Informe um valor: ')))

mai = max(lista)
men = min(lista)

print(f'O maior valor da lista é: {mai}, localizado nas posições: ',end='')
for i,v in enumerate(lista):
    if lista[i] == mai:
        print(f'{i}...',end='')

print(f'\nO menor valor da lista é: {men}, localizado nas posições: ',end='')
for i,v in enumerate(lista):
    if lista[i] == men:
        print(f'{i}...',end='')
