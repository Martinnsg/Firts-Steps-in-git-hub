#faça um código que leia o peso de varias pessoas. No final coloque quantas pessoas foram cadastradas e qual o maior e o menor peso
lista = []
galera = []
maior = menor = 0
#===============================================================================================
import os
while True:
    os.system('cls')
    galera.append(str(input('Qual é o seu nome? ')))
    galera.append(int(input('Qual é o seu peso? ')))
#===============================================================================================   
    if len(lista) == 0:
        maior = menor = galera[1]
    else:
        if galera[1] > maior:
            maior = galera[1]
        elif galera [1] < menor:
            menor = galera [1]
            #menor = galera [1]
#===============================================================================================
    lista.append(galera[:])
    galera.clear()
    n = str(input('Deseja adicionar mais uma pessoa? [S/N]: ')).upper()
    if n == 'N':
        break
#===============================================================================================
os.system('cls')
print(f'Foram cadastradas {len(lista)} pessoas.\n')
print(f'O maior peso foi {maior}Kg de:',end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}...',end='')

print(f'\nO menor peso foi {menor}Kg de:',end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}...',end='')
             
    



