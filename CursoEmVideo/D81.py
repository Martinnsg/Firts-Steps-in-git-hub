#crie um programa que vai ler varios numeros e colocar em uma lista
#a) mostre quantos numeros foram digitados
#b) mostre a lista de forma decrescente
#c) se o valor 5 foi digitado e esta ou nao na lista
import os
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    n = str(input('Deseja adicionar outro número? [S/N]: ')).upper()
    if n == 'N':
        os.system('cls')
        lista.sort(reverse = True)
        print(f'A lista inserida foi: {lista}')
        print(f'A lista teve {len(lista)} números inseridos.')
        if 5 in lista:
            print('O valor 5 faz parte da lista')
        else:
            print('O valor 5 não faz parte da lista')
        break
    