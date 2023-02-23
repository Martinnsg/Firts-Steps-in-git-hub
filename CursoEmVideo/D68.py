#par ou impar, interromper se o jogador perder
import random
import os
t = 0
c = 0

while True:
    y = random.randint(0,10)
    print('MINI-GAME: PAR OU ÍMPAR')
    n = int(input('Digite um valor: '))
    x = str(input('Par ou ímpar? [P/I] ')).upper()
    c = n + y
    #print(f'{n} + {y} = {c}')
    # c = c/2
    # print(f'C/2 = {c}')
    #print(c%2)
    if(c%2 == 0):
        #print(f'Você jogou {n} e o computador {y}. Total: {c}, deu par')
        if (x=='P'):
            print('Você venceu!')
            t += 1
            os.system('cls')
        elif(x=='I'):
            os.system('cls')
            print('Você perdeu!')
            print(f'Número de vitorias: {t}')   
            break
    elif(c%2 != 0):
        #print(f'Você jogou {n} e o computador {y}. Total: {c}, deu impar')        
        if (x=='I'):
            print('Você venceu!')
            t += 1
            os.system('cls')
        elif(x=='P'):
            os.system('cls')
            print('Você perdeu!')
            print(f'Número de vitorias: {t}')    
            break  

