#faça um código que leia uma expressão com parenteses e verifique se ela é valida atraves da quantidade de parenteses

exp = str(input('Digite uma expressão:'))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é invalida')