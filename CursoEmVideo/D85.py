#crie um programa que leia 7 valores e armazene em duas listas dentro de uma lista, os valores pares e impares
lista = [[],[]]
import os

for i in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista[0].append(n)
    elif n % 2 == 1:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()
os.system('cls')
if len(lista[0]) == 0:
    print('Não foi digitado nenhum valor par')
else:
    print(f'Os números pares digitados foram: {lista[0]}')

if len(lista[1]) == 0:
    print('Não foi digitado nenhum valor ímpar')
else:
    print(f'Os números ímpares digitados foram: {lista[1]}')




    