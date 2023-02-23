#programa contador personalizado
from time import sleep
def cont1(n,m,x):
    print('-='*30)
    print(f'Contagem de {n} até {m}, pulando de {x} em {x}')
    if m<n:
        x = -x
        m = m-1
    if m > n:
        m = m+1
    for i in range(n,m,x):
        print(i,end=' ')
        sleep(1)
    print('FIM!')
cont1(0,10,1)
cont1(10,0,2)
print('-='*30)
n = int(input('Inicio: '))
m = int(input('Fim: '))
x = int(input('Passo: '))
cont1(n,m,x)