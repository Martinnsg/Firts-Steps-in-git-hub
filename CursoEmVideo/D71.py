#crie um caixa eletronico. Perguntar o valor a ser sacado e o caixa informe a quantidade de notas que ele ira 
while True:
    print('{:=^40}'.format(' CAIXA ELETRONICO '))
    v = int(input('Informe o valor que deseja sacar: R$'))

#contador de nota de 50
    d = v//50
    c50 = d
    n50 = d * 50
    res = v - n50

#contador de nota de 20
    d = res//20
    c20 = d
    n20 = d * 20
    res = res - n20

#contador de nota de 10
    d = res//10
    c10 = d
    n10 = d * 10
    res = res - n10

#contador de nota de 1
    d = res//1
    c1 = d
    n1 = d * 1
    res = res - n1

    print(f'Para entregar o valor de R${v} foram necessarias: \n{c50} notas de 50, \n{c20} notas de 20, \n{c10} notas de 10 \n{c1} notas de 1')

    break