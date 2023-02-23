#crie um programa onde o usario digite varios valores e os cadastre em uma lista. caso o numero ja esteja na lista ele não será adicionado
import os
lista = []
while True:
    n = int(input('Digite um valor:'))
    if n in lista:
        print('O valor ja existe na lista!')
    else:
        lista.append(n)
    d = str(input('Deseja inserir outro valor? [S/N]: ')).upper()
    if d == 'N':
        os.system('cls')
        lista.sort()
        print (f'Todos os números digitados em ordem crescente foram: {lista}')
        break


