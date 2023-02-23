aluno = dict()
aluno ['nome'] = str(input('Nome: '))
aluno ['média'] = float(input('Média: '))
print(f'O aluno {aluno["nome"]} teve uma média de {aluno["média"]}.')

if aluno['média'] >= 6:
    print('O aluno foi aprovado!')
else: 
    print('O aluno foi reprovado')