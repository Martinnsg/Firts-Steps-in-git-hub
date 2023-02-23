#crie um programa que leia o nome e o preço de cada produto. informe o total gasto. informe quantos produtos custam mais de 1000. informe o produto mais barato
import os
total = pr1 = menor = cont = 0
barato = ' '
while True:
    p = str(input('Informe o nome do produto: '))
    pr = float(input('Informe o preço do produto: '))
    cont += 1
    total += pr

    if (pr > 1000):
        pr1 += 1

#bloco para salvar o menor preço
    if (cont == 1):         #assim que iniciar a primeira vez, contador vai salvar em 1
        menor = pr          #a variavel menor vai receber o preço atual
        barato = p          #a str barato vai receber o nome do produto atual
    else:
        if pr < menor:      #se o preço for menor que o menor preço salvo
            menor = pr      #o menor vai receber o preço atual
            barato = p      #salva o nome do produto atual

    c = ' '
    while c not in 'SN':
        c = str(input('Deseja continuar inserindo? [S/N]: ')).upper()
    
    if (c == 'S'):
        os.system('cls')
    elif (c == 'N'):
        # print(f'{} produtos custam mais de R$1000,00')
        # print(f'O total gasto dessa lista é de R${}')
        # print(f'O produto mais barato da lista é o {} custando {}')
        os.system('cls')
        print('{:-^40}'.format(' FIM DO PROGRAMA '))
        print(f'O preço total do programa foi R${total:.2f}')
        print(f'O total de produtos que custam mais de R$1000,00 foram: {pr1}')
        print(f'O produto mais barato é o/a {barato}, custando R${menor}')
        break
