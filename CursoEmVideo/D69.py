 #faça um programa que leia idade e sexo de varias pessoas. quantas pessoas com mais de 18, quantas mulheres com mais de 20 e quantos homens
import os
xi=xm=xh=0
while True:
    i = int(input('Informe sua idade:'))
    s = ' '
    while s not in 'HM':
        s = str(input('Informe seu sexo [H/M]: ')).upper()
    n = ' '
    while n not in 'SN':
        n = str(input('Deseja incluir mais uma pessoa? [S/N]: ')).upper()
    if (i>=18):
        xi += 1
    if (s=='H'):
        xh += 1
    if (s=='M' and i<20):
        xm += 1

    if (n=='N'):
        os.system('cls')
        print(f'\nForam cadastrados {xi} pessoas maiores de 18 anos')
        print(f'Foram cadastrados {xm} mulheres menores de 20 anos')
        print(f'Foram cadastrados {xh} homens\n')
        break
    elif (n=='S'):
        os.system('cls')

