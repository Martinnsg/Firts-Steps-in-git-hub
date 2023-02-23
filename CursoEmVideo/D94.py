#unindo dicionarios e listas
#leia nome e idade e coloque se deseja continuar ou não
import os
idade = 0
lista = list()
listamolieres = list()
while True:
   
    dic = {'nome':'','sexo':'','idade':0}
    dic['nome'] = str(input('Nome: '))    
    while (dic['sexo'] != 'M') and (dic['sexo'] !='F'):
        dic['sexo'] = str(input('Sexo [M/F]: ')).upper()
    if dic['sexo'] ==  'F':
        listamolieres.append(dic['nome'])
    dic['idade'] = int(input('Idade: '))
    idade += dic['idade']
    lista.append(dic.copy())
    media = idade / len(lista)

    cond = str(input('Deseja continuar? [S/N]: ')).upper() 
    while cond not in 'NS':
        cond = str(input('Deseja continuar? [S/N]: ')).upper() 
    dic.clear()

    if cond == 'N':
        break

os.system('cls')
print('-='*30)
print(f'A) Foram cadastradas {len(lista)} pessoas.')
print(f'B) A idade média das pessoas cadastradas é de: {media}')
print(f'C) Lista das mulheres cadastradas: {listamolieres}')
print('D) Lista das pessoas com idade acima da média: ')
for i in range (0,len(lista)):
    if lista[i]['idade'] > media:
        print(lista[i])
print('-='*30)