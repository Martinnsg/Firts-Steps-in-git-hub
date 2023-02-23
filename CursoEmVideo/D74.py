#crie um programa que gere 5 numeros aleatorios e coloque em uma tupla
#mostre a listagem dos numeros gerados, indique o menor e o maior
from random import randint
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'A tupla gerada é: {n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')