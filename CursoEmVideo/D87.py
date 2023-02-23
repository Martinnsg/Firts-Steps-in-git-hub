#aprimore o desafio anterior mostrando no final
#a soma de todos os valores pares
#a soma dos valores da terceira coluna
#o maior valor da segunda linha
soma = col3 = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range (0,3):
    for j in range (0,3):
        matriz[i][j] = int(input(f'Digite um valor para [{i},{j}]: '))
        if matriz [i][j] % 2 == 0:
            soma += matriz[i][j]

for i in range (0,3):
    col3 += matriz[i][2]

maior = matriz[1][0]
for i in range (0,3):
    if matriz [1][i] > maior:
        maior = matriz[1][i]

print('-='*30)
for i in range (0,3):
    for j in range (0,3):
        print(f'[{matriz[i][j]}]', end='')
    print()

print(f'A soma de todos os valores da ultima coluna é: {col3}')
print(f'A soma de todos os valores pares da matriz é: {soma}')
print(f'O maior valor da segunda linha é: {maior}')