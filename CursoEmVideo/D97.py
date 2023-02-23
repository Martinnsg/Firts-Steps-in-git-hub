#um print especial
def escreva(msg):
    tam = len(msg)
    print('~'*(tam + 4))
    print(' ',msg)
    print('~'*(tam + 4))  

msg = str(input('Digite algo: '))
escreva(msg)