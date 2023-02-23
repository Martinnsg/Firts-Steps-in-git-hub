lista = ('Makita', 500, 'Bosch', 450, 'deWalt', 700, 'Milwalkee', 1000)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for pos in range (0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')

print('-'*40)