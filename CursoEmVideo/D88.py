#jogo da mega sena
from time import sleep
from random import randint
lista = []
jogos = []

print('-'*30)
print('      JOGO DA MEGA SENA     ')
print('-'*30)
tot = 1
n = int(input('Quantos jogos você quer sortear: '))

while tot <=n:
    cont = 0
 
    if n == 0:
        break
    while True: 
        r = randint(1,60)
        if r not in lista:
            lista.append(r)
            cont += 1
        if cont >= 6:
            break
    lista.sort()       
    jogos.append(lista[:])
    lista.clear()
    tot +=1

    
print('-=' * 3, f' SORTEANDO {n} JOGOS ', '-='*3)
print()
for i in range (0,n):
    print(f'Jogo {i+1}: {jogos[i]}')
    sleep(1)
print()  
print('-='*4, f' < BOA SORTE! > ', '-=' * 4)


