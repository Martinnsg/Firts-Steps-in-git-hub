#faça um código que insira nome e nota de varios alunos, depois, te de a opção de ver a nota do aluno informado
nomes = list()
nota1 = list()
nota2 = list()
import os
while True:

    nomes.append(str(input('Nome: ')).lower())
    nota1.append(float(input('Nota 1: ')))
    nota2.append(float(input('Nota 2: ')))
    n = str(input('Quer continuar? [S/N]: ')).upper()
    if n == 'N':
        break

os.system('cls')
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i in range (len(nomes)):
    print(f' {i:<4}{nomes[i]:<10}{(nota1[i] + nota2[i]) / 2:>8}')
print('-'*60)

while True:
    mostrar = str(input('Mostrar notas de qual aluno? ')).lower()
    if mostrar in nomes:
        i = nomes.index(mostrar)
        print(f'Notas de {mostrar} são: {nota1[i]} e {nota2[i]}')
    if mostrar == 'del':
        break
    if mostrar not in nomes:
        print('O aluno não está na planilha de notas!')
    


# print (nomes[0])
# print (nota1)
# print (nota2)

