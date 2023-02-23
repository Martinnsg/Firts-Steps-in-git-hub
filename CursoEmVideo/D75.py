#desenvolva um codigo que leia 4 valores inteiros e salve-os em uma tupla
n = (int(input('Digite um primeiro número: ')),
    int(input('Digite um segundo número: ')),
    int(input('Digite um terceiro número: ')),
    int(input('Digite um ultimo número: ')))

if n.count(9) == 0:
    print('Não foi digitado nenhum número 9')
else:
    print(f'Foram digitados {n.count(9)} números 9')

if n.count(3) == 0:
    print('Não foi digitado nenhum número 3')
else:
    print(f'A primeira aparição do número 3 foi na posição {n.index(3)}')

print('Os números pares digitados foram: ',end='')
for num in n:
    if num % 2 == 0:
        print(num, end =' ')