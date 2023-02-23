#matriz 3x3
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range (0,3):
    for j in range (0,3):
        matriz[i][j] = int(input(f'Digite um valor para [{i},{j}]: '))

print('-='*30)
for i in range (0,3):
    for j in range (0,3):
        print(f'[{matriz[i][j]}]', end='')
    print()
# for j in range (0,3):
#     matriz[1].append(int(input(f'Digite um valor para [1,{i}]: ')))
# for k in range (0,3):
#     matriz[2].append(int(input(f'Digite um valor para [2,{i}]: ')))
# for l in range (0,9):
#     print(f'{matriz}')


