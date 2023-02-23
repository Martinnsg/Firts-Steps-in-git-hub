#analise qual valor é o maior
from time import sleep
def maior(* núm):
    print('-='*30)
    print('ANALISANDO VALORES...')
    cont = 0
    for i in núm:
        print(i,end=' ')
        sleep(0.5)
        if cont == 0:
            m = i
        elif i>m:
            m = i
        cont +=1
    print(f'O maior valor digitado foi: {m}')    

maior(99,87,56,32,78,23)
maior(10,22,35,2,7)
maior(182,200345,3,1,0)
maior(0)
maior(1,2,3,4,5,6,1000)