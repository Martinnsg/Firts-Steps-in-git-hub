#crie um programa que leia varios valores e interrompa quando o numero for 999. Mostre quantos numeros foram digitados e a soma deles
c = 0
ct = 0
while True:
    n = int(input('Informe um número:'))
    if (n==999):
        print('\nFim do programa.')
        print(f'A soma dos numeros informados é: {c}, fora digitados {ct} números.')
        break
    else:
        ct += 1
        c += n
