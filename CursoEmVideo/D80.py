#crie um programa que o usuario insira 5 valores e cadastre na posição certa de inserção
lista = []
for c in range (0,5):
    n = int(input('Digite um número: '))
    if c == 0:
        lista.append(n)
        print('Valor adicionado no final da lista')
    elif n > lista[-1]:
        lista.append(n)
        print('Valor adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Valor adicionado na posição {pos} da lista')
                break
            pos += 1

print('-='*30)
print(f'{lista}')