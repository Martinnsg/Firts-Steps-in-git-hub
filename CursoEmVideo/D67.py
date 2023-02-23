#faça um código de tabuada em while, que seja parado com numero negativo

while True:
    n = int(input('Informe o número que deseja ver a tabuada: '))
    if (n < 0):
        print('\nTabuada desligada.\n')
        break
    else:
        for i in range (0,11):
            t = n * i
            print (f'{n} * {i} = {t}')
        print('\n')